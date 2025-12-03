from navigate.model.device_startup_functions import device_not_found

DEVICE_TYPE_NAME = "camera"  # Same as in configuraion.yaml, for example "stage", "filter_wheel", "remote_focus_device"...
DEVICE_REF_LIST = ["type"]  # the reference value from configuration.yaml
SUPPORTED_DEVICE_TYPES = ["MyCamera"]

def load_device(hardware_configuration, is_synthetic=False, device_type=None):
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
    if hardware_configuration["type"] == "MyCamera":
        from .camera import MyCamera
        return MyCamera.connect(hardware_configuration["serial_number"])
    else:
        return type("DeviceConnection", (object,), {})


def start_device(microscope_name, device_connection, configuration, *args, is_synthetic=False, id=0, **kwargs):
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
            "camera"
        ]["hardware"]["type"]

    if device_type == "MyCamera":
        # install through navigate
        # plugin_device = load_module_from_file(
        #     "plugin_device",
        #     os.path.join(Path(__file__).resolve().parent, "plugin_device.py"),
        # )
        # return plugin_device.PluginDevice(device_connection=device_connection)

        # install through pip
        from .camera import MyCamera
        return MyCamera(microscope_name, device_connection, configuration)
    elif device_type.lower() == "synthetic":
        # install through navigate
        # synthetic_device = load_module_from_file(
        #     "synthetic_device",
        #     os.path.join(Path(__file__).resolve().parent, "synthetic_device.py"),
        # )
        # return synthetic_device.SyntheticDevice(device_connection=device_connection)
    
        # install through pip
        from navigate.model.devices.camera.synthetic import SyntheticCamera
        return SyntheticCamera(microscope_name, device_connection, configuration)
    else:
        return device_not_found(microscope_name, device_type)
