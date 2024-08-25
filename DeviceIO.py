# All referenced (missing descriptions)
from typing import Callable


class DeviceIO:
    """
    This class represents a specific input or output bus of a device.
    """
    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def available_routing_channels(self):
        """
        :return: Get the available routing channels for the DeviceIO.
        """
        return []

    @property
    def available_routing_types(self):
        """
        :return: Get the available routing types for the DeviceIO.
        """
        return []

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the DeviceIO.
        """
        return None

    @property
    def default_external_routing_channel_is_none(self) -> bool:
        """
        Get and set whether the default routing channel for External routing types is none.
        """
        return False

    @property
    def routing_channel(self):
        """
        Get and set the current routing channel.
        Raises ValueError if the channel isn't one of the current values in available_routing_channels.
        """
        return

    @property
    def routing_type(self):
        """
        Get and set the current routing type.
        Raises ValueError if the type isn't one of the current values in available_routing_types.
        """
        return

    def add_available_routing_channels_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_routing_channels" has changed.
        """
        return

    def add_available_routing_types_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_routing_types" has changed.
        """
        return

    def add_routing_channel_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "routing_channel" has changed.
        """
        return

    def add_routing_type_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "routing_type" has changed.
        """
        return

    def available_routing_channels_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_routing_channels".
        """
        return False

    def available_routing_types_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_routing_types".
        """
        return False

    def remove_available_routing_channels_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_routing_channels".
        """
        return

    def remove_available_routing_types_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_routing_types".
        """
        return

    def remove_routing_channel_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "routing_channel".
        """
        return

    def remove_routing_type_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "routing_type".
        """
        return

    def routing_channel_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "routing_channel".
        """
        return False

    def routing_type_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "routing_type".
        """
        return False
