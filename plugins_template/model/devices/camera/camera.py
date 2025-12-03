
import time
from typing import Any, Optional, List
import ctypes

import numpy as np

from navigate.model.devices.camera.base import CameraBase
from navigate.model.concurrency.concurrency_tools import SharedNDArray
from navigate.model.analysis import camera

class MyCamera(CameraBase):
    def __init__(
        self,
        microscope_name: str,
        device_connection: Any,
        configuration: dict[str, Any],
        *args: Optional[Any],
        **kwargs: Optional[Any],
    ) -> None:
        super().__init__(
            microscope_name, device_connection, configuration, *args, **kwargs
        )
        #: bool: Whether the camera is currently acquiring
        self.is_acquiring = False

        #: int: mean background count for synthetic image
        self._mean_background_count = 100

        #: float: noise sigma for synthetic image
        self._noise_sigma = camera.compute_noise_sigma()

        #: int: current image id
        self.current_frame_idx = None

        #: object: data buffer
        self.data_buffer = None

        #: int: number of frames
        self.num_of_frame = None

        #: int: previous image id
        self.pre_frame_idx = None

        #: bool: whether to use random image
        self.random_image = True

        #: int: serial number
        self.serial_number = "synthetic"

        #: float: exposure time
        self.camera_exposure_time = 0.2

        #: int: x binning
        self.x_binning = 1

        #: int: y binning
        self.y_binning = 1

        #: int: width
        self.x_pixels = self.camera_parameters["x_pixels"]

        #: int: height
        self.y_pixels = self.camera_parameters["y_pixels"]

        #: int: center x
        self.center_x = self.x_pixels // 2

        #: int: center y
        self.center_y = self.y_pixels // 2

        #: int: current image id
        self.img_id = 0

        #: int: current tif id
        self.current_tif_id = 0

        self.camera_parameters["supported_trigger_sources"] = ["External", "Internal"]

    @classmethod
    def connect(cls, serial_number: str) -> Any:
        """Connect to MyCamera camera.

        Parameters
        ----------
        serial_number : str
            Camera serial number.

        Returns
        -------
        device_connection : object
            Device connection object.
        """
        # Here you would implement the actual connection logic to the camera hardware.
        # For this example, we'll just return a dummy object.
        return type("DeviceConnection", (object,), {"serial_number": serial_number})()

    def set_ROI(
        self,
        roi_width: int = 2048,
        roi_height: int = 2048,
        center_x: int = 1024,
        center_y: int = 1024,
    ) -> bool:
        return True
    
    def set_binning(self, binning: str = "1x1") -> bool:
        return True
    
    def set_trigger_mode(self, trigger_source: str = "External") -> None:
        """Set the camera trigger source to external or internal free run mode.

        This abstract method must be implemented by all subclasses.

        Parameters
        ----------
        trigger_source : str
            Trigger source. Options are 'External' or 'Internal'.
        """
        pass

    def set_sensor_mode(self, mode: str) -> None:
        """Set camera sensor mode.

        Parameters
        ----------
        mode : str
            Sensor mode. Options are 'Normal' or 'Light-Sheet'.
        """
        pass

    def set_exposure_time(self, exposure_time: float) -> None:
        """Set SyntheticCamera exposure time.

        All of our units are in milliseconds. Function converts to seconds.

        Parameters
        ----------
        exposure_time : float
            Exposure time in seconds.
        """
        self.camera_exposure_time = exposure_time

    def set_line_interval(self, line_interval_time: float) -> bool:
        """Set SyntheticCamera line interval.

        Parameters
        ----------
        line_interval_time : float
            Line interval duration.
        """
        super().set_line_interval(line_interval_time)

    def set_binning(self, binning_string: str) -> bool:
        """Set SyntheticCamera binning mode.

        Parameters
        ----------
        binning_string : str
            Desired binning properties (e.g., '2x2', '4x4', '8x8')

        Returns
        -------
        bool
            True if successful, False otherwise.
        """
        binning_dict = {
            "1x1": 1,
            "2x2": 2,
            "4x4": 4,
            # '8x8': 8,
            # '16x16': 16,
            # '1x2': 102,
            # '2x4': 204
        }
        if binning_string not in binning_dict.keys():
            print(f"can't set binning to {binning_string}")
            return False

        self.x_binning = int(binning_string[0])
        self.y_binning = int(binning_string[2])
        self.x_pixels = int(self.x_pixels / self.x_binning)
        self.y_pixels = int(self.y_pixels / self.y_binning)
        return True

    def initialize_image_series(
        self,
        data_buffer: Optional[List[SharedNDArray]] = None,
        number_of_frames: int = 100,
    ) -> None:
        """Initialize SyntheticCamera image series.

        Parameters
        ----------
        data_buffer : Optional[List[SharedNDArray]]
            The shared data buffer. Default is None.
        number_of_frames : int
            Number of frames.  Default is 100.
        """
        # prpare the camera for image acquisition
        self.data_buffer = data_buffer
        self.num_of_frame = number_of_frames
        self.current_frame_idx = 0
        self.pre_frame_idx = 0
        self.is_acquiring = True

    def close_image_series(self) -> None:
        """Close image series.

        Stops the acquisition and sets is_acquiring flag to False.
        """
        self.pre_frame_idx = 0
        self.current_frame_idx = 0
        self.is_acquiring = False

    def generate_new_frame(self) -> None:
        """Generate a synthetic image."""
        # A software trigger would normally be sent to the camera here
        print("Generating new frame in MyCamera")
        if not self.is_acquiring:
            return
        if self.random_image:
            image = np.random.normal(
                0,
                self._noise_sigma
                / 0.47,  # TODO: Don't hardcode 0.47 electrons per count
                size=(self.x_pixels, self.y_pixels),
            ).astype(np.uint16) + int(self._mean_background_count)
        else:
            image = self.tif_images[self.current_tif_id][self.img_id]
            self.img_id += 1
            if self.img_id >= len(self.tif_images[self.current_tif_id]):
                self.img_id = 0
                self.current_tif_id = (self.current_tif_id + 1) % len(self.tif_images)

        ctypes.memmove(
            self.data_buffer[self.current_frame_idx].ctypes.data,
            image.ctypes.data,
            self.x_pixels * self.y_pixels * 2,
        )

        self.current_frame_idx = (self.current_frame_idx + 1) % self.num_of_frame

    def get_new_frame(self) -> List[int]:
        """Get frame from SyntheticCamera camera."""

        time.sleep(self.camera_exposure_time)
        timeout = 500
        while self.pre_frame_idx == self.current_frame_idx and timeout:
            time.sleep(0.001)
            timeout -= 1
        if timeout <= 0:
            return []
        if self.pre_frame_idx < self.current_frame_idx:
            frames = list(range(self.pre_frame_idx, self.current_frame_idx))
        else:
            frames = list(range(self.pre_frame_idx, self.num_of_frame))
            frames += list(range(0, self.current_frame_idx))
        self.pre_frame_idx = self.current_frame_idx
        return frames
    
    @staticmethod
    def calculate_readout_time() -> float:
        """Calculate duration of time needed to read out an image.

        Calculates the readout time and maximum frame rate according to the camera
        configuration settings.

        Returns
        -------
        readout_time : float
            Duration of time needed to read out an image.
        """
        readout_time = 0.01  # 10 milliseconds.
        return readout_time
    
    def calculate_light_sheet_exposure_time(
        self, full_chip_exposure_time: float, shutter_width: float
    ) -> tuple[float, float, float]:
        """Calculate the light sheet exposure time.

        Parameters
        ----------
        full_chip_exposure_time : float
            Full chip exposure time in seconds.
        shutter_width : float
            Shutter width in pixels.

        Returns
        -------
        tuple[float, float, float]
            Tuple containing the light sheet exposure time, the line interval time,
            and the readout time.
        """
        (
            exposure_time,
            camera_line_interval,
            full_chip_exposure_time,
        ) = super().calculate_light_sheet_exposure_time(
            full_chip_exposure_time, shutter_width
        )

        return exposure_time, camera_line_interval, full_chip_exposure_time

    def set_readout_direction(self, mode) -> None:
        super().set_readout_direction(mode)

