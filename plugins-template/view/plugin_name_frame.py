# Standard Imports
import tkinter as tk
from tkinter import ttk


class PluginNameFrame(ttk.Frame):
    """Plugin Frame: Just an example

    This frame contains the widgets for the plugin.
    """

    def __init__(self, root, *args, **kwargs):
        """Initilization of the  Frame

        Parameters
        ----------
        root : tkinter.ttk.Frame
            The frame that this frame will be placed in.
        *args
            Variable length argument list.
        **kwargs
            Arbitrary keyword arguments.
        """
        ttk.Frame.__init__(self, root, *args, **kwargs)

        # Formatting
        tk.Grid.columnconfigure(self, "all", weight=1)
        tk.Grid.rowconfigure(self, "all", weight=1)

        # Dictionary for widgets and buttons
        #: dict: Dictionary of the widgets in the frame
        self.inputs = {}
        self.buttons = {}
        self.variables = {}

        # #################################
        # ######## Example Widgets ########
        # ##### add your widgets here #####
        # #################################
        label = ttk.Label(self, text="Plugin Name:")
        label.grid(row=0, column=0, sticky=tk.NW)

        self.variables["plugin_name"] = tk.StringVar(self)
        self.inputs["plugin_name"] = ttk.Entry(
            self, textvariable=self.variables["plugin_name"]
        )
        self.inputs["plugin_name"].grid(
            row=0, column=1, sticky="N", padx=5, pady=(0, 5)
        )

        self.buttons["move"] = ttk.Button(self, text="MOVE")
        self.buttons["move"].grid(row=1, column=1, sticky="N", padx=6)

    # Getters
    def get_variables(self):
        """Returns a dictionary of the variables for the widgets in this frame.

        The key is the widget name, value is the variable associated.

        Returns
        -------
        variables : dict
            Dictionary of the variables for the widgets in this frame.
        """
        return self.variables

    def get_widgets(self):
        """Returns a dictionary of the widgets in this frame.

        The key is the widget name, value is the LabelInput class that has all the data.

        Returns
        -------
        self.inputs : dict
            Dictionary of the widgets in this frame.
        """
        return self.inputs
