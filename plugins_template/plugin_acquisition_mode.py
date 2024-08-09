from navigate.tools.decorators import AcquisitionMode
from navigate.model.features.feature_related_functions import (
    ExampleFeature,
)


@AcquisitionMode
class PluginAcquisitionMode:
    def __init__(self, name):
        self.acquisition_mode = name

        self.feature_list = [{"name": ExampleFeature}]

    def prepare_acquisition_controller(self, controller):
        """Controller side preparation before acquisition

        Parameters
        ----------
        controller : object
            navigate controller
        """
        print("*** prepare controller before acquisition!")
        pass

    def end_acquisition_controller(self, controller):
        """Controller side cleanup after acquisition

        Parameters
        ----------
        controller : object
            navigate controller
        """
        print("*** end acquisition")
        pass

    def prepare_acquisition_model(self, model):
        """Model side preparation before acquisition

        Parameters
        ----------
        model : object
            navigate model
        """
        print("*** prepare model before acquisition!")
        pass

    def end_acquisition_model(self, model):
        """Model side cleanup after acquisition

        Parameters
        ----------
        model : object
            navigate model
        """
        print("*** end acquisition model")
        pass
