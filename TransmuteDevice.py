# All referenced (missing descriptions)
from typing import Callable
from Live.Device import Device


class TransmuteDevice(Device):
    """
    This class represents a Transmute device.
    """
    @property
    def frequency_dial_mode_index(self) -> int:
        """
        Return the current frequency dial mode index
        """
        return 0

    @property
    def frequency_dial_mode_list(self):
        """
        Return the current frequency dial mode list
        """
        return

    @property
    def midi_gate_index(self) -> int:
        """
        Return the current midi gate index
        """
        return 0

    @property
    def midi_gate_list(self):
        """
        Return the current midi gate list
        """
        return

    @property
    def mod_mode_index(self) -> int:
        """
        Return the current mod mode index
        """
        return 0

    @property
    def mod_mode_list(self):
        """
        Return the current mod mode list
        """
        return

    @property
    def mono_poly_index(self) -> int:
        """
        Return the current mono poly mode index
        """
        return 0

    @property
    def mono_poly_list(self):
        """
        Return the current mono poly mode list
        """
        return

    @property
    def pitch_bend_range(self) -> int:
        """
        Return the current pitch bend range
        """
        return 0

    @property
    def pitch_mode_index(self) -> int:
        """
        Return the current pitch mode index
        """
        return 0

    @property
    def pitch_mode_list(self):
        """
        Return the current pitch mode list
        """
        return

    @property
    def polyphony(self) -> int:
        """
        Return the current polyphony
        """
        return 0

    def add_frequency_dial_mode_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "frequency_dial_mode_index" has changed.
        """
        pass

    def add_frequency_dial_mode_list_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "frequency_dial_mode_list" has changed.
        """
        pass

    def add_midi_gate_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "midi_gate_index" has changed.
        """

    def add_midi_gate_list_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "midi_gate_list" has changed.
        """
        pass

    def add_mod_mode_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mod_mode_index" has changed.
        """
        pass

    def add_mod_mode_list_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mod_mode_list" has changed.
        """
        pass

    def add_mono_poly_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mono_poly_index" has changed.
        """
        pass

    def add_mono_poly_list_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mono_poly_list" has changed.
        """
        pass

    def add_pitch_bend_range_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "pitch_bend_range" has changed.
        """
        pass

    def add_pitch_mode_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "pitch_mode_index" has changed.
        """
        pass

    def add_pitch_mode_list_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "pitch_mode_list" has changed.
        """
        pass

    def add_polyphony_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "polyphony" has changed.
        """
        pass

    def frequency_dial_mode_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "frequency_dial_mode_index".
        """
        return False

    def frequency_dial_mode_list_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "frequency_dial_mode_list".
        """
        return False

    def midi_gate_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "midi_gate_index".
        """
        return False

    def midi_gate_list_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "midi_gate_list".
        """
        return False

    def mod_mode_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mod_mode_index".
        """
        return False

    def mod_mode_list_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mod_mode_list".
        """
        return False

    def mono_poly_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mono_poly_index".
        """

    def mono_poly_list_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mono_poly_list".
        """
        return False

    def pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "pitch_bend_range".
        """
        return False

    def pitch_mode_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "pitch_mode_index".
        """
        return False

    def pitch_mode_list_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "pitch_mode_list".
        """
        return False

    def polyphony_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "polyphony".
        """
        return False

    def remove_frequency_dial_mode_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "frequency_dial_mode_index".
        """
        pass

    def remove_frequency_dial_mode_list_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "frequency_dial_mode_list".
        """
        pass

    def remove_midi_gate_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "midi_gate_index".
        """
        pass

    def remove_midi_gate_list_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "midi_gate_list".
        """
        pass

    def remove_mod_mode_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mod_mode_index".
        """
        pass

    def remove_mod_mode_list_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mod_mode_list".
        """
        pass

    def remove_mono_poly_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mono_poly_index".
        """
        pass

    def remove_mono_poly_list_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mono_poly_list".
        """
        pass

    def remove_pitch_bend_range_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "pitch_bend_range".
        """
        pass

    def remove_pitch_mode_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "pitch_mode_index".
        """
        pass

    def remove_pitch_mode_list_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "pitch_mode_list".
        """
        pass

    def remove_polyphony_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "polyphony".
        """
        pass
