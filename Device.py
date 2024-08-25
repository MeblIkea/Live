# All referenced (missing descriptions)
from typing import Callable
from Live.Base import Vector


class ATimeableValueVector(Vector):
    pass


class DeviceType:
    audio_effect = None
    instrument = None
    midi_effect = None
    undefined = None


class Device:
    """
    This class represents a MIDI or Audio DSP-Device in Live.
    """
    class View:
        @property
        def _live_ptr(self) -> int:
            """
            :return: Get the pointer to the Live Object.
            """
            return 0

        @property
        def canonical_parent(self):
            """
            :return: Get the canonical parent of the Device.View.
            """
            return None

        @property
        def is_collapsed(self) -> bool:
            """
            :return: Get/Set/Listen if the device view is collapsed.
            """
            return False

        def add_is_collapsed_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
            """
            pass

        def is_collapsed_has_listener(self, arg2: Callable) -> bool:
            """
            :return: if the given listener function or method is connected to the property "is_collapsed".
            """
            pass

        def remove_is_collapsed_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "is_collapsed".
            """
            pass

    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def can_have_chains(self) -> bool:
        """
        :return: if the device is a rack.
        """
        return False

    @property
    def can_have_drum_pads(self) -> bool:
        """
        :return: if the device is a drum rack.
        """
        return False

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the Device.
        """
        return None

    @property
    def class_display_name(self) -> str:
        """
        :return: Const access to the name of the device's class name as displayed in Live's browser and device chain
        """
        return ""

    @property
    def class_name(self) -> str:
        """
        :return: Const access to the name of the device's class.
        """
        return ""

    @property
    def is_active(self) -> bool:
        """
        :return: Const access to whether this device is active. This will be false both when the device is off and when it's inside a rack device which is off.
        """
        return False

    @property
    def name(self) -> str:
        """
        :return: Access to the name of the device.
        """
        return ""

    @property
    def parameters(self) -> ATimeableValueVector:
        """
        :return: Const access to the list of available automatable parameters for this device.
        """
        return ATimeableValueVector()

    @property
    def type(self) -> DeviceType:
        """
        :return: Type of the device as DeviceType.
        """
        return DeviceType()

    @property
    def view(self) -> View:
        """
        :return: Representing the view aspects of a device.
        """
        return self.View()

    def add_is_active_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "is_active" has changed.
        """
        pass

    def add_name_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        pass

    def add_parameters_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "parameters" has changed.
        """
        pass

    def is_active_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_active".
        """
        return False

    def name_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        return False

    def parameters_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "parameters".
        """
        return False

    def remove_is_active_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_active".
        """
        pass

    def remove_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        pass

    def remove_parameters_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "parameters".
        """
        pass

    def store_chosen_bank(self, arg2: int, arg3: int):
        """
        Set the selected bank in the device for persistency.
        """
        pass
