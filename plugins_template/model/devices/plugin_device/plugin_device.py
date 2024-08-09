class PluginDevice:
    def __init__(self, device_connection, *args):
        pass

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"move_plugin_device": lambda *args: self.move(args[0])}

    def move(self, *args):
        """An example function: to move the device"""
        print("move device", args)
        pass
