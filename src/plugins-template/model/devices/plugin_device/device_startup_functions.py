# Standard Imports
import importlib

from .plugin_device import PluginDevice
from .synthetic_device import SyntheticDevice
from navigate.model.device_startup_functions import device_not_found

DEVICE_TYPE_NAME = "plugin_device"  # Same as in configuraion.yaml, for example "stage", "filter_wheel", "remote_focus_device"...
DEVICE_REF_LIST = ["type"]  # the reference value from configuration.yaml


def load_device(configuration, is_synthetic=False):
    """Build device connection.

    Returns
    -------
    device_connection : object
    """
    return type("DeviceConnection", (object,), {})


def start_device(microscope_name, device_connection, configuration, is_synthetic=False):
    """Start device. 
    
    Returns
    -------
    device_object : object
    """
    if is_synthetic:
        device_type = "synthetic"
    else:
        device_type = configuration["configuration"]["microscopes"][microscope_name][
            "plugin_device"
        ]["hardware"]["type"]

    if device_type == "PluginDevice":
        return PluginDevice(device_connection=device_connection)
    elif device_type == "synthetic":
        return SyntheticDevice()
    else:
        return device_not_found(microscope_name, device_type)
