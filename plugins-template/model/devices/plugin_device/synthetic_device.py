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
        return {}