# All referenced (missing descriptions)
from typing import Callable
from Live.Device import Device


class CompressorDevice(Device):
    """
    This class represents a Compressor device.
    """
    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0

    @property
    def available_input_routing_channels(self):
        """
        :return: list of source channels for input routing in the side chain.
        """
        return

    @property
    def available_input_routing_types(self):
        """
        :return: list of source types for input routing in the side chain.
        """
        return

    @property
    def input_routing_channel(self):
        """
        :return: the current source channel for input routing in the side chain.
        """
        return

    @property
    def input_routing_type(self):
        """
        :return: the current source type for input routing in the side chain.
        """
        return

    def add_available_input_routing_channels_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_input_routing_channels" has changed.
        """
        return

    def add_available_input_routing_types_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_input_routing_types" has changed.
        """
        return

    def add_input_routing_channel_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_routing_channel" has changed.
        """
        return

    def add_input_routing_type_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_routing_type" has changed.
        """
        return

    def available_input_routing_channels_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_input_routing_channels".
        """
        return False

    def available_input_routing_types_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_input_routing_types".
        """
        return False

    def input_routing_channel_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_routing_channel".
        """
        return False

    def input_routing_type_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_routing_type".
        """
        return False

    def remove_available_input_routing_channels_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_input_routing_channels".
        """
        return

    def remove_available_input_routing_types_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_input_routing_types".
        """
        return

    def remove_input_routing_channel_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_routing_channel".
        """
        return

    def remove_input_routing_type_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_routing_type".
        """
        return
