# Have to finish Rack Device
from typing import Callable
from Live.Device import Device


class RackDevice(Device):
    """
    This class represents a Rack device.
    """
    class View(Device.View):
        """
        Representing the view aspects of a rack device.
        """
        @property
        def drum_pads_scroll_position(self) -> int:
            """
            Throws an exception if can_have_drum_pads is false.
            :return: Access to the index of the lowest visible row of pads.
            """
            return 0

        @property
        def is_showing_chain_devices(self) -> bool:
            """
            Throws an exception if can_have_chains is false.
            :return: Return whether the devices in the currently selected chain are visible.
            """
            return False

        @property
        def selected_chain(self):
            """
            :return: Return access to the currently selected chain.
            """
            return

        @property
        def selected_drum_pad(self):
            """
            Throws an exception if can_have_drum_pads is false.
            :return: Return access to the currently selected drum pad.
            """
            return

        def add_drum_pads_scroll_position_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "drum_pads_scroll_position" has changed.
            """
            return

        def add_is_showing_chain_devices_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "is_showing_chain_devices" has changed.
            """

        def add_selected_chain_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "selected_chain" has changed.
            """
            return

        def add_selected_drum_pad_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "selected_drum_pad" has changed.
            """

        def drum_pads_scroll_position_has_listener(self, arg2: Callable) -> bool:
            """
            :return: If the given listener function or method is connected to the property "drum_pads_scroll_position".
            """
            return False

        def is_showing_chain_devices_has_listener(self, arg2: Callable) -> bool:
            """
            :return: If the given listener function or method is connected to the property "is_showing_chain_devices".
            """
            return False

        def remove_drum_pads_scroll_position_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "drum_pads_scroll_position".
            """

        def remove_is_showing_chain_devices_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "is_showing_chain_devices".
            """
            return

        def remove_selected_chain_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "selected_chain".
            """

        def remove_selected_drum_pad_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "selected_drum_pad".
            """
            return

        def selected_chain_has_listener(self, arg2: Callable) -> bool:
            """
            :return: If the given listener function or method is connected to the property "selected_chain".
            """
            return False

        def selected_drum_pad_has_listener(self, arg2: Callable) -> bool:
            """
            :return: If the given listener function or method is connected to the property "selected_drum_pad".
            """
            return False

