class SyntheticDevice:
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
            "move_plugin_device": lambda *args: print(
                f"move synthetic plugin device {args[0]}!"
            )
        }
