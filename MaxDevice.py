# All referenced (missing descriptions)
from typing import Callable
from Live.Device import Device


class MaxDevice(Device):
    """
    This class represents a Max for Live device.
    """
    @property
    def audio_inputs(self):
        """
        Const access to a list of all audio inputs in the device.
        """
        return

    @property
    def audio_outputs(self):
        """
        Const access to a list of all audio outputs in the device.
        """
        return

    @property
    def midi_inputs(self):
        """
        Const access to a list of all MIDI inputs in the device.
        """
        return

    @property
    def midi_outputs(self):
        """
        Const access to a list of all MIDI outputs in the device.
        """
        return

    def add_audio_inputs_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "audio_inputs" has changed.
        """
        return

    def add_audio_outputs_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "audio_outputs" has changed.
        """
        return

    def add_bank_parameters_changed_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "bank_parameters_changed" has changed.
        """
        return

    def add_midi_inputs_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "midi_inputs" has changed.
        """
        return

    def add_midi_outputs_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "midi_outputs" has changed.
        """
        return

    def audio_inputs_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "audio_inputs".
        """
        return False

    def audio_outputs_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "audio_outputs".
        """
        return False

    def bank_parameters_changed_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "bank_parameters_changed".
        """
        return False

    def get_bank_count(self) -> int:
        """
        :return: The number of parameter banks.
        """
        return 0

    def get_bank_name(self, arg2: int) -> str:
        """
        :return: Retrieves the number of parameter banks, related to hardware control surfaces.
        """
        return ""

    def get_bank_parameters(self, arg2: int):
        """
        :return: Retrieves the indices of parameters using the given bank index.
        """

    def get_value_item_icons(self, arg2):
        """
        :return: Retrieves a list of icon identifier strings for a list parameter's values.
        """
        return

    def midi_inputs_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "midi_inputs".
        """
        return False

    def midi_outputs_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "midi_outputs".
        """
        return False

    def remove_audio_inputs_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "audio_inputs".
        """
        return

    def remove_audio_outputs_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "audio_outputs".
        """
        return

    def remove_bank_parameters_changed_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "bank_parameters_changed".
        """
        return

    def remove_midi_inputs_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "midi_inputs".
        """
        return

    def remove_midi_outputs_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "midi_outputs".
        """
        return
