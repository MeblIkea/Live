# All referenced (missing descriptions)
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

    @property
    def can_show_chains(self) -> bool:
        """
        :return: True if this Rack contains a rack instrument device
        that is capable of showing its chains in session view.
        """
        return False

    @property
    def chains(self):
        """
        :return: Return const access to the list of chains in this device.
        """
        return

    @property
    def drum_pads(self):
        """
        :return: Return const access to the list of drum pads in this device.
        """
        return

    @property
    def has_drum_pads(self) -> bool:
        """
        :return: Returns true if the device is a drum rack which has drum pads.
        """
        return False

    @property
    def has_macro_mappings(self) -> bool:
        """
        :return: Returns true if any of the rack's macros are mapped to a parameter.
        """
        return False

    @property
    def is_showing_chains(self) -> bool:
        """
        :return: Returns True, if it is showing chains.
        """
        return False

    @property
    def macros_mapped(self):
        """
        :return: A list of booleans, one for each macro parameter, which is True iff
        that macro is mapped to something.
        """
        return

    @property
    def return_chains(self):
        """
        :return: Return const access to the list of return chains in this device.
        """
        return

    @property
    def selected_variation_index(self) -> int:
        """
        :return: Access to the index of the currently selected macro variation.
        """
        return 0

    @property
    def variation_count(self) -> int:
        """
        :return: Access to the number of macro variations currently stored.
        """
        return 0

    @property
    def visible_drum_pads(self):
        """
        :return: Return const access to the list of visible drum pads in this device.
        """
        return

    def add_chains_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "chains" has changed.
        """
        return

    def add_drum_pads_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "drum_pads" has changed.
        """
        return

    def add_has_drum_pads_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_drum_pads" has changed.
        """
        return

    def add_has_macro_mappings_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_macro_mappings" has changed.
        """
        return

    def add_is_showing_chains_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "is_showing_chains" has changed.
        """
        return

    def add_macro(self):
        """
        Increases the number of visible macro controls in the rack.
        Throws an exception if the maximum number of macro controls is reached.
        """
        return

    def add_macros_mapped_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "macros_mapped" has changed.
        """
        return

    def add_return_chains_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "return_chains" has changed.
        """
        return

    def add_visible_drum_pads_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "visible_drum_pads" has changed.
        """
        return

    def chains_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "chains".
        """
        return False

    def copy_pad(self, source_index: int, destination_index: int):
        """
        Copies all contents of a drum pad from a source pad into a destination pad.
        Copy_pad(source_index, destination_index)
        where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack.
        Throws an exception when the source pad is empty,
        or when the source or destination indices are not between 0-127.
        """
        return

    def delete_selected_variation(self):
        """
        Deletes the currently selected macro variation.
        Does nothing if there is no selected variation.
        """
        return

    def drum_pads_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "drum_pads".
        """
        return False

    def has_drum_pads_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "has_drum_pads".
        """
        return False

    def has_macro_mappings_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "has_macro_mappings".
        """
        return False

    def is_showing_chains_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "is_showing_chains".
        """
        return False

    def macros_mapped_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "macros_mapped".
        """
        return False

    def randomize_macros(self):
        """
        Randomizes the values for all macro controls not excluded from randomization.
        """
        return

    def recall_last_used_variation(self):
        """
        Recalls the macro variation recalled most recently.
        Does nothing if no variation has been recalled yet.
        """
        return

    def recall_selected_variation(self):
        """
        Recalls the currently selected macro variation.
        Does nothing if there are no variations.
        """
        return

    def remove_chains_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "chains".
        """
        return

    def remove_drum_pads_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "drum_pads".
        """
        return

    def remove_has_drum_pads_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_drum_pads".
        """
        return

    def remove_has_macro_mappings_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_macro_mappings".
        """
        return

    def remove_is_showing_chains_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_showing_chains".
        """
        return

    def remove_macro(self):
        """
        Decreases the number of visible macro controls in the rack.
        Throws an exception if the minimum number of macro controls is reached.
        """
        return

    def remove_macros_mapped_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "macros_mapped".
        """
        return

    def remove_return_chains_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "return_chains".
        """
        return

    def remove_visible_drum_pads_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "visible_drum_pads".
        """
        return

    def return_chains_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "return_chains".
        """
        return False

    def store_variation(self):
        """
        Stores a new variation of the values of all currently mapped macros
        """
        return

    def visible_drum_pads_has_listener(self, arg2: Callable) -> bool:
        """
        :return: Returns true, if the given listener function or method is connected to the property "visible_drum_pads".
        """
        return False
