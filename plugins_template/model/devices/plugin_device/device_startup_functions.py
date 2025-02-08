# Standard Imports
import os
from pathlib import Path

from navigate.tools.common_functions import load_module_from_file
from navigate.model.device_startup_functions import device_not_found

DEVICE_TYPE_NAME = "plugin_device"  # Same as in configuraion.yaml, for example "stage", "filter_wheel", "remote_focus_device"...
DEVICE_REF_LIST = ["type"]  # the reference value from configuration.yaml
SUPPORTED_DEVICE_TYPES = ["PluginDevice", "Synthetic"]

def load_device(hardware_configuration, is_synthetic=False):
    """Build device connection.

    Parameters
    ----------
    hardware_configuration : dict
        device hardware configuration section
    is_synthetic : bool
        use synthetic hardware

    Returns
    -------
    device_connection : object
    """
    return type("DeviceConnection", (object,), {})


def start_device(microscope_name, device_connection, configuration, is_synthetic=False):
    """Start device.

    Parameters
    ----------
    microscope_name : string
        microscope name
    device_connection : object
        device connection object returned by load_device()
    configuration : dict
        navigate configuration
    is_synthetic : bool
        use synthetic hardware

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
        # install through navigate
        # plugin_device = load_module_from_file(
        #     "plugin_device",
        #     os.path.join(Path(__file__).resolve().parent, "plugin_device.py"),
        # )
        # return plugin_device.PluginDevice(device_connection=device_connection)

        # install through pip
        from .plugin_device import PluginDevice
        return PluginDevice(device_connection=device_connection)
    elif device_type.lower() == "synthetic":
        # install through navigate
        # synthetic_device = load_module_from_file(
        #     "synthetic_device",
        #     os.path.join(Path(__file__).resolve().parent, "synthetic_device.py"),
        # )
        # return synthetic_device.SyntheticDevice(device_connection=device_connection)
    
        # install through pip
        from .synthetic_device import SyntheticDevice
        return SyntheticDevice(device_connection=device_connection)
    else:
        return device_not_found(microscope_name, device_type)
