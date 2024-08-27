from typing import Callable

from Live.Base import StringVector


class EffectMode:
    frequency_modulation = None
    none = None
    sync_and_pulse_width = None
    warp_and_fold = None


class FilterRouting:
    parallel = None
    serial = None
    split = None


class ModulationSource:
    amp_envelope = None
    envelope_2 = None
    envelope_3 = None
    lfo_1 = None
    lfo_2 = None
    midi_channel_pressure = None
    midi_mod_wheel = None
    midi_note = None
    midi_pitch_bend = None
    midi_random = None
    midi_velocity = None


class UnisonMode:
    classic = None
    fast_shimmer = None
    none = None
    phase_sync = None
    position_spread = None
    random_note = None
    slow_shimmer = None


class VoiceCount:
    eight = None
    five = None
    four = None
    seven = None
    six = None
    three = None
    two = None


class Voicing:
    mono = None
    poly = None


class WavetableDevice:
    """
    This class represents a Wavetable Device in Live.
    """
    @property
    def filter_routing(self) -> FilterRouting:
        """
        Return the current filter routing.
        """
        return FilterRouting()

    @property
    def mono_poly(self) -> Voicing:
        """
        Return the current voicing mode.
        """
        return Voicing()

    @property
    def oscillator_1_effect_mode(self) -> EffectMode:
        """
        Return the current effect mode of the oscillator 1.
        """
        return EffectMode()

    @property
    def oscillator_1_wavetable_category(self) -> str:
        """
        Return the current wavetable category of the oscillator 1.
        """
        return ""

    @property
    def oscillator_1_wavetable_index(self) -> int:
        """
        Return the current wavetable index of the oscillator 1.
        """
        return 0

    @property
    def oscillator_1_wavetables(self) -> StringVector:
        """
        Get a vector of oscillator 1's wavetable names.
        """
        return StringVector()

    @property
    def oscillator_2_effect_mode(self) -> EffectMode:
        """
        Return the current effect mode of the oscillator 2.
        """
        return EffectMode()

    @property
    def oscillator_2_wavetable_category(self) -> str:
        """
        Return the current wavetable category of the oscillator 2.
        """
        return ""

    @property
    def oscillator_2_wavetable_index(self) -> int:
        """
        Return the current wavetable index of the oscillator 2.
        """
        return 0

    @property
    def oscillator_2_wavetables(self) -> StringVector:
        """
        Get a vector of oscillator 2's wavetable names.
        """
        return StringVector()

    @property
    def oscillator_wavetable_categories(self) -> StringVector:
        """
        Get a vector of the available wavetable categories.
        """
        return StringVector()

    @property
    def poly_voices(self) -> VoiceCount:
        """
        Return the current number of polyphonic voices. Uses the VoiceCount enumeration.
        """
        return VoiceCount()

    @property
    def unison_mode(self) -> UnisonMode:
        """
        Return the current unison mode.
        """
        return UnisonMode()

    @property
    def unison_voice_count(self) -> int:
        """
        Return the current number of unison voices.
        """
        return 0

    @property
    def visible_modulation_target_names(self) -> StringVector:
        """
        Get the names of all the visible modulation targets.
        """
        return StringVector()

    def add_filter_routing_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "filter_routing" has changed.
        """
        return

    def add_modulation_matrix_changed_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "modulation_matrix_changed" has changed.
        """
        return

    def add_mono_poly_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mono_poly" has changed.
        """
        return

    def add_oscillator_1_effect_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_1_effect_mode" has changed.
        """
        return

    def add_oscillator_1_wavetable_category_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetable_category" has changed.
        """
        return

    def add_oscillator_1_wavetable_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetable_index" has changed.
        """
        return

    def add_oscillator_1_wavetables_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetables" has changed.
        """
        return

    def add_oscillator_2_effect_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_2_effect_mode" has changed.
        """
        return

    def add_oscillator_2_wavetable_category_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetable_category" has changed.
        """
        return

    def add_oscillator_2_wavetable_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetable_index" has changed.
        """
        return

    def add_oscillator_2_wavetables_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetables" has changed.
        """
        return

    def add_parameter_to_modulation_matrix(self, parameter) -> int:
        """
        Add a non-pitch parameter to the modulation matrix.
        """
        return 0

    def add_poly_voices_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "poly_voices" has changed.
        """
        return

    def add_unison_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "unison_mode" has changed.
        """
        return

    def add_unison_voice_count_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "unison_voice_count" has changed.
        """
        return

    def add_visible_modulation_target_names_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "visible_modulation_target_names" has changed.
        """
        return

    def filter_routing_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "filter_routing".
        """
        return False

    def get_modulation_target_parameter_name(self, target_index) -> str:
        """
        Get the parameter name of the modulation target at the given index.
        """
        return ""

    def get_modulation_value(self, target_index, source) -> float:
        """
        Get the value of a modulation amount for the given target-source connection.
        """
        return 0.0

    def is_parameter_modulatable(self, parameter) -> bool:
        """
        Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there.
        """
        return False

    def modulation_matrix_changed_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "modulation_matrix_changed".
        """
        return False

    def mono_poly_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mono_poly".
        """
        return False

    def oscillator_1_effect_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_1_effect_mode".
        """
        return False

    def oscillator_1_wavetable_category_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetable_category".
        """
        return False

    def oscillator_1_wavetable_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetable_index".
        """
        return False

    def oscillator_1_wavetables_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetables".
        """
        return False

    def oscillator_2_effect_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_2_effect_mode".
        """
        return False

    def oscillator_2_wavetable_category_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetable_category".
        """
        return False

    def oscillator_2_wavetable_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetable_index".
        """
        return False

    def oscillator_2_wavetables_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetables".
        """
        return False

    def poly_voices_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "poly_voices".
        """
        return False

    def remove_filter_routing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "filter_routing".
        """
        return

    def remove_modulation_matrix_changed_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "modulation_matrix_changed".
        """
        return

    def remove_mono_poly_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mono_poly".
        """
        return

    def remove_oscillator_1_effect_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_1_effect_mode".
        """
        return

    def remove_oscillator_1_wavetable_category_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_1_wavetable_category".
        """
        return

    def remove_oscillator_1_wavetable_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_1_wavetable_index".
        """
        return

    def remove_oscillator_1_wavetables_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_1_wavetables".
        """
        return

    def remove_oscillator_2_effect_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_2_effect_mode".
        """
        return

    def remove_oscillator_2_wavetable_category_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_2_wavetable_category".
        """
        return

    def remove_oscillator_2_wavetable_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_2_wavetable_index".
        """
        return

    def remove_oscillator_2_wavetables_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "oscillator_2_wavetables".
        """
        return

    def remove_poly_voices_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "poly_voices".
        """
        return

    def remove_unison_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "unison_mode".
        """
        return

    def remove_unison_voice_count_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "unison_voice_count".
        """
        return

    def remove_visible_modulation_target_names_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "visible_modulation_target_names".
        """
        return

    def set_modulation_value(self, target_index, source, value):
        """
        Set the value of a modulation amount for the given target-source connection.
        """
        return

    def unison_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "unison_mode".
        """
        return False

    def unison_voice_count_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "unison_voice_count".
        """
        return False

    def visible_modulation_target_names_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "visible_modulation_target_names".
        """
        return False
