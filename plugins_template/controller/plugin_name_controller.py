class PluginNameController:
    def __init__(self, view, parent_controller=None):
        self.view = view
        self.parent_controller = parent_controller
        
        self.variables = self.view.get_variables()
        self.buttons = self.view.buttons

        # #################################
        # ##### Example Widget Events #####
        # #################################
        self.buttons["move"].configure(command=self.move)

    def move(self, *args):
        """Example function to move the plugin device
        """

        print("*** Move button is clicked!")
        self.parent_controller.execute("move_plugin_device", self.variables["plugin_name"].get())


    