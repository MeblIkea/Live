# All referenced (missing descriptions)
from typing import Callable
from Live.Device import Device


class GlobalMode:
    left_right = None
    mid_side = None
    stereo = None


class EditMode:
    a = None
    b = None


class Eq8Device(Device):
    """
    This class represents an Eq8 device.
    """
    class View(Device.View):
        """
        Representing the view aspects of an Eq8 device.
        """
        @property
        def selected_band(self):
            """
            :return: The selected band.
            """
            return

        def add_selected_band_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "selected_band" has changed.
            """
            return

        def remove_selected_band_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "selected_band".
            """
            return

        def selected_band_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_band".
            """
            return False

    @property
    def edit_mode(self):
        """
        :return: Access to Eq8's edit mode.
        """
        return

    @property
    def global_mode(self):
        """
        :return: Access to Eq8's global mode.
        """
        return

    @property
    def oversample(self):
        """
        :return: Access to Eq8's oversample value.
        """
        return

    def add_edit_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "edit_mode" has changed.
        """
        return

    def add_global_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "global_mode" has changed.
        """
        return

    def add_oversample_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oversample" has changed.
        """
        return

    def edit_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "edit_mode".
        """
        return False

    def global_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "global_mode".
        """
        return False

    def oversample_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oversample".
        """
        return False

    def remove_edit_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "edit_mode".
        """
        return

    def remove_global_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "global_mode".
        """
        return

    def remove_oversample_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oversample".
        """
        return
