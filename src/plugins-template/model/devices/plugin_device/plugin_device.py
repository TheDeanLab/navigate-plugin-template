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
        return {
            "move_plugin_device": self.move
        }
    
    def move(self, *args):
        """An example function: to move the device

        """
        print("move device", args)
        pass