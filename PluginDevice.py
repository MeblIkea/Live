# All referenced (missing descriptions)
from typing import Callable
from Live.Base import StringVector
from Live.Device import Device


class PluginDevice(Device):
    """
    This class represents a plugin device.
    """

    @property
    def presets(self):
        """
        Get the list of presets the plugin offers.
        """
        return []

    @property
    def selected_preset_index(self) -> int:
        """
        Access to the index of the currently selected preset.
        """
        return 0

    def add_presets_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "presets" has changed.
        """
        return

    def add_selected_preset_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "selected_preset_index" has changed.
        """
        return

    def get_parameter_names(self, begin: int = 0, end: int = -1) -> StringVector:
        """
        Get the range of plugin parameter names, bound by beginning and end.
        If the end is smaller than 0, it is interpreted as the parameter counts.
        """
        return StringVector()

    def presets_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "presets".
        """
        return False

    def remove_presets_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "presets".
        """
        return

    def remove_selected_preset_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "selected_preset_index".
        """
        return

    def selected_preset_index_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "selected_preset_index".
        """
        return False
