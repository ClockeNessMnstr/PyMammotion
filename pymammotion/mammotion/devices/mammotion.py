"""Device control of mammotion robots over bluetooth or MQTT."""

from __future__ import annotations

import asyncio
import logging
from enum import Enum
from functools import cache
from typing import Any

from aiohttp import ClientSession
from bleak.backends.device import BLEDevice

from pymammotion.aliyun.cloud_gateway import CloudIOTGateway
from pymammotion.aliyun.dataclass.dev_by_account_response import Device
from pymammotion.const import MAMMOTION_DOMAIN
from pymammotion.data.model.account import Credentials
from pymammotion.data.model.device import MowingDevice
from pymammotion.http.http import connect_http
from pymammotion.mammotion.devices.mammotion_bluetooth import MammotionBaseBLEDevice
from pymammotion.mammotion.devices.mammotion_cloud import MammotionBaseCloudDevice, MammotionCloud
from pymammotion.mqtt import MammotionMQTT

TIMEOUT_CLOUD_RESPONSE = 10

_LOGGER = logging.getLogger(__name__)


class ConnectionPreference(Enum):
    """Enum for connection preference."""

    EITHER = 0
    WIFI = 1
    BLUETOOTH = 2


class MammotionMixedDeviceManager:
    _ble_device: MammotionBaseBLEDevice | None = None
    _cloud_device: MammotionBaseCloudDevice | None = None
    _mowing_state: MowingDevice
    preference: ConnectionPreference

    def __init__(
        self,
        name: str,
        cloud_device: Device | None = None,
        ble_device: BLEDevice | None = None,
        mqtt: MammotionCloud | None = None,
        preference: ConnectionPreference = ConnectionPreference.BLUETOOTH,
    ) -> None:
        self.name = name
        self._mowing_state = MowingDevice()
        self.add_ble(ble_device)
        self.add_cloud(cloud_device, mqtt)
        self.preference = preference

    def mower_state(self):
        return self._mowing_state

    def ble(self) -> MammotionBaseBLEDevice | None:
        return self._ble_device

    def cloud(self) -> MammotionBaseCloudDevice | None:
        return self._cloud_device

    def add_ble(self, ble_device: BLEDevice) -> None:
        if ble_device is not None:
            self._ble_device = MammotionBaseBLEDevice(self._mowing_state, ble_device)

    def add_cloud(self, cloud_device: Device | None = None, mqtt: MammotionCloud | None = None) -> None:
        if cloud_device is not None:
            self._cloud_device = MammotionBaseCloudDevice(
                mqtt, cloud_device=cloud_device, mowing_state=self._mowing_state
            )

    def replace_cloud(self, cloud_device: MammotionBaseCloudDevice) -> None:
        self._cloud_device = cloud_device

    def replace_ble(self, ble_device: MammotionBaseBLEDevice) -> None:
        self._ble_device = ble_device

    def replace_mqtt(self, mqtt: MammotionCloud) -> None:
        self._cloud_device._mqtt = mqtt

    def has_cloud(self) -> bool:
        return self._cloud_device is not None

    def has_ble(self) -> bool:
        return self._ble_device is not None


class MammotionDevices:
    devices: dict[str, MammotionMixedDeviceManager] = {}

    def add_device(self, mammotion_device: MammotionMixedDeviceManager) -> None:
        exists: MammotionMixedDeviceManager | None = self.devices.get(mammotion_device.name)
        if exists is None:
            self.devices[mammotion_device.name] = mammotion_device
            return
        if mammotion_device.has_cloud():
            exists.replace_cloud(mammotion_device.cloud())
        if mammotion_device.has_ble():
            exists.replace_ble(mammotion_device.ble())

    def get_device(self, mammotion_device_name: str) -> MammotionMixedDeviceManager:
        return self.devices.get(mammotion_device_name)

    def remove_device(self, name) -> None:
        device_for_removal = self.devices.pop(name)
        if device_for_removal.has_cloud():
            should_disconnect = {
                device
                for key, device in self.devices.items()
                if device.cloud() is not None and device.cloud()._mqtt == device_for_removal.cloud()._mqtt
            }
            if len(should_disconnect) == 0:
                device_for_removal.cloud()._mqtt.disconnect()


async def create_devices(
    ble_device: BLEDevice,
    cloud_credentials: Credentials | None = None,
    preference: ConnectionPreference = ConnectionPreference.BLUETOOTH,
):
    mammotion = Mammotion()
    mammotion.add_ble_device(ble_device, preference)

    if cloud_credentials and preference == ConnectionPreference.EITHER or preference == ConnectionPreference.WIFI:
        await mammotion.login_and_initiate_cloud(
            cloud_credentials.account_id or cloud_credentials.email, cloud_credentials.password
        )

    return mammotion


@cache
class Mammotion:
    """Represents a Mammotion account and its devices."""

    devices = MammotionDevices()
    mqtt_list: dict[str, MammotionCloud] = dict()

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initialize MammotionDevice."""
        self._login_lock = asyncio.Lock()

    def add_ble_device(
        self, ble_device: BLEDevice, preference: ConnectionPreference = ConnectionPreference.BLUETOOTH
    ) -> None:
        if ble_device:
            self.devices.add_device(
                MammotionMixedDeviceManager(name=ble_device.name, ble_device=ble_device, preference=preference)
            )

    async def login_and_initiate_cloud(self, account, password, force: bool = False) -> None:
        async with self._login_lock:
            exists: MammotionCloud | None = self.mqtt_list.get(account)
            if not exists or force:
                cloud_client = await self.login(account, password)
            else:
                cloud_client = exists.cloud_client

            await self.initiate_cloud_connection(account, cloud_client)

    async def initiate_cloud_connection(self, account: str, cloud_client: CloudIOTGateway) -> None:
        if self.mqtt_list.get(account) is not None:
            if self.mqtt_list.get(account).is_connected:
                # we might have removed a device so readd
                self.add_cloud_devices(self.mqtt_list.get(account))
                return

        self.cloud_client = cloud_client
        mammotion_cloud = MammotionCloud(
            MammotionMQTT(
                region_id=cloud_client.region_response.data.regionId,
                product_key=cloud_client.aep_response.data.productKey,
                device_name=cloud_client.aep_response.data.deviceName,
                device_secret=cloud_client.aep_response.data.deviceSecret,
                iot_token=cloud_client.session_by_authcode_response.data.iotToken,
                client_id=cloud_client.client_id,
                cloud_client=cloud_client,
            ),
            cloud_client,
        )
        self.mqtt_list[account] = mammotion_cloud
        self.add_cloud_devices(mammotion_cloud)

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, self.mqtt_list[account].connect_async)

    def add_cloud_devices(self, mqtt_client: MammotionCloud) -> None:
        for device in mqtt_client.cloud_client.devices_by_account_response.data.data:
            mower_device = self.devices.get_device(device.deviceName)
            if device.deviceName.startswith(("Luba-", "Yuka-")) and mower_device is None:
                self.devices.add_device(
                    MammotionMixedDeviceManager(
                        name=device.deviceName,
                        cloud_device=device,
                        mqtt=mqtt_client,
                        preference=ConnectionPreference.WIFI,
                    )
                )
            elif device.deviceName.startswith(("Luba-", "Yuka-")) and mower_device:
                if mower_device.cloud() is None:
                    mower_device.add_cloud(cloud_device=device, mqtt=mqtt_client)
                elif mqtt_client != mower_device.cloud().mqtt:
                    mower_device.replace_mqtt(mqtt_client)

    def set_disconnect_strategy(self, disconnect: bool) -> None:
        for device_name, device in self.devices.devices:
            if device.ble() is not None:
                ble_device: MammotionBaseBLEDevice = device.ble()
                ble_device.set_disconnect_strategy(disconnect)

    async def login(self, account: str, password: str) -> CloudIOTGateway:
        """Login to mammotion cloud."""
        cloud_client = CloudIOTGateway()
        async with ClientSession(MAMMOTION_DOMAIN) as session:
            mammotion_http = await connect_http(account, password)
            country_code = mammotion_http.login_info.userInformation.domainAbbreviation
            _LOGGER.debug("CountryCode: " + country_code)
            _LOGGER.debug("AuthCode: " + mammotion_http.login_info.authorization_code)
            loop = asyncio.get_running_loop()
            cloud_client.set_http(mammotion_http)
            await loop.run_in_executor(
                None, cloud_client.get_region, country_code, mammotion_http.login_info.authorization_code
            )
            await cloud_client.connect()
            await cloud_client.login_by_oauth(country_code, mammotion_http.login_info.authorization_code)
            await loop.run_in_executor(None, cloud_client.aep_handle)
            await loop.run_in_executor(None, cloud_client.session_by_auth_code)

            await loop.run_in_executor(None, cloud_client.list_binding_by_account)
            return cloud_client

    def remove_device(self, name: str) -> None:
        self.devices.remove_device(name)

    def get_device_by_name(self, name: str) -> MammotionMixedDeviceManager:
        return self.devices.get_device(name)

    async def send_command(self, name: str, key: str):
        """Send a command to the device."""
        device = self.get_device_by_name(name)
        if device:
            if device.preference is ConnectionPreference.BLUETOOTH:
                return await device.ble().command(key)
            if device.preference is ConnectionPreference.WIFI:
                return await device.cloud().command(key)
            # TODO work with both with EITHER

    async def send_command_with_args(self, name: str, key: str, **kwargs: Any):
        """Send a command with args to the device."""
        device = self.get_device_by_name(name)
        if device:
            if device.preference is ConnectionPreference.BLUETOOTH:
                return await device.ble().command(key, **kwargs)
            if device.preference is ConnectionPreference.WIFI:
                return await device.cloud().command(key, **kwargs)
            # TODO work with both with EITHER

    async def start_sync(self, name: str, retry: int):
        device = self.get_device_by_name(name)
        if device:
            if device.preference is ConnectionPreference.BLUETOOTH:
                return await device.ble().start_sync(retry)
            if device.preference is ConnectionPreference.WIFI:
                return await device.cloud().start_sync(retry)
            # TODO work with both with EITHER

    async def start_map_sync(self, name: str):
        device = self.get_device_by_name(name)
        if device:
            if device.preference is ConnectionPreference.BLUETOOTH:
                return await device.ble().start_map_sync()
            if device.preference is ConnectionPreference.WIFI:
                return await device.cloud().start_map_sync()
            # TODO work with both with EITHER

    def mower(self, name: str):
        device = self.get_device_by_name(name)
        if device:
            return device.mower_state()
