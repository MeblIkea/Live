from typing import Any, Callable

from Live.Base import Vector


class DeviceContainer:
    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0


class DeviceInsertMode:
    count = None
    default = None
    selected_left = None
    selected_right = None


class RoutingChannelLayout:
    midi = None
    mono = None
    stereo = None


class RoutingChannel:
    @property
    def display_name(self) -> str:
        """
        Get the display name of the routing channel.
        """
        return ""

    @property
    def layout(self) -> RoutingChannelLayout:
        """
        Get the routing channel's Layout, e.g., mono or stereo.
        """
        return RoutingChannelLayout()


class RoutingChannelVector(Vector):
    def append(self, arg2: RoutingChannel) -> None:
        """
        Append a routing channel to the vector.
        """
        return


class RoutingTypeCategory:
    external = None
    internal = None
    master = None
    none = None
    parent_group_track = None
    resampling = None
    rewire = None
    track = None


class RoutingType:
    """
    This class represents a routing type.
    """
    @property
    def attached_object(self):
        """
        Live object associated with the routing type.
        """
        return Any()

    @property
    def category(self) -> RoutingTypeCategory:
        """
        Get the routing type's category.
        """
        return RoutingTypeCategory()

    @property
    def display_name(self) -> str:
        """
        Get the display name of the routing type.
        """
        return ""


class RoutingTypeVector(Vector):
    def append(self, arg2: RoutingType) -> None:
        """
        Append a routing type to the vector.
        """
        return


class Track:
    class monitoring_states:
        IN = None
        OFF = None
        AUTO = None

    class View:
        """
        Representing the view aspects of a Track.
        """
        @property
        def _live_ptr(self) -> int:
            """
            Get the pointer to the Live Object.
            """
            return 0

        @property
        def canonical_parent(self):
            """
            Get the canonical parent of the track view.
            """
            return Track()

        @property
        def device_insert_mode(self) -> DeviceInsertMode:
            """
            Get/Listen the device insertion mode of the track.
            """
            return DeviceInsertMode.default

        @property
        def is_collapsed(self) -> bool:
            """
            Get/Set/Listen if the track is shown collapsed in the arranger view.
            """
            return False

        @property
        def selected_device(self) -> Any:
            """
            Get/Set/Listen the insertion mode of the device. While in insertion mode, loading new devices from the browser will place devices at the selected position.
            """
            return Any()

        def add_device_insert_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "device_insert_mode" has changed.
            """
            return

        def add_is_collapsed_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
            """
            return

        def add_selected_device_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "selected_device" has changed.
            """
            return

        def device_insert_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "device_insert_mode".
            """
            return False

        def is_collapsed_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_collapsed".
            """
            return False

        def remove_device_insert_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "device_insert_mode".
            """
            return

        def remove_is_collapsed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_collapsed".
            """
            return

        def remove_selected_device_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "selected_device".
            """
            return

        def select_instrument(self) -> bool:
            """
            Selects the track's instrument if it has one.
            """
            return False

        def selected_device_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_device".
            """
            return False

    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0

