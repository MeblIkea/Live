# All referenced (missing descriptions)
from typing import Callable


class SlicingBeatDivision:
    eighth = None
    eighth_triplett = None
    four_bars = None
    half = None
    half_triplett = None
    one_bar = None
    quarter = None
    quarter_triplett = None
    sixteenth = None
    sixteenth_triplett = None
    two_bars = None


class SlicingStyle:
    beat = None
    manual = None
    region = None
    transient = None


class TransientLoopMode:
    alternate = None
    forward = None
    off = None


class Sample:
    """
    This class represents a sample file loaded into a Simpler instance.
    """
    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def beats_granulation_resolution(self):
        """
        :return: Access to the Granulation Resolution parameter in Beats Warp Mode.
        """
        return

    @property
    def beats_transient_envelope(self):
        """
        :return: Access to the Transient Envelope parameter in Beats Warp Mode.
        """
        return

    @property
    def beats_transient_loop_mode(self):
        """
        :return: Access to the Transient Loop Mode parameter in Beats Warp Mode.
        """
        return

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the Sample.
        """
        return

    @property
    def complex_pro_envelope(self):
        """
        :return: Access to the Envelope parameter in Complex Pro Mode.
        """
        return

    @property
    def complex_pro_formants(self):
        """
        :return: Access to the Formants parameter in Complex Pro Warp Mode.
        """
        return

    @property
    def end_marker(self):
        """
        :return: Access to the position of the sample's end marker.
        """
        return

    @property
    def file_path(self):
        """
        :return: Get the path of the sample file.
        """
        return

    @property
    def gain(self):
        """
        :return: Access to the sample gain.
        """
        return

    @property
    def length(self) -> int:
        """
        :return: Get the length of the sample file in sample frames.
        """
        return 0

    @property
    def sample_rate(self) -> int:
        """
        :return: Access to the audio sample rate of the sample.
        """
        return 0

    @property
    def slices(self):
        """
        :return: Access to the list of slice points in sample time in the sample.
        """
        return

    @property
    def slicing_beat_division(self) -> SlicingBeatDivision:
        """
        :return: Access to sample's slicing step size.
        """
        return SlicingBeatDivision()

    @property
    def slicing_region_count(self) -> int:
        """
        :return: Access to sample's slicing split count.
        """
        return 0

    @property
    def slicing_sensitivity(self) -> float:
        """
        :return: Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0.The higher the sensitivity, the more slices will be available.
        """
        return 0.0

    @property
    def slicing_style(self) -> SlicingStyle:
        """
        :return: Access to sample's slicing style.
        """
        return SlicingStyle()

    @property
    def start_marker(self):
        """
        :return: Access to the position of the sample's start marker.
        """
        return

    @property
    def texture_flux(self):
        """
        :return: Access to the Flux parameter in Texture Warp Mode.
        """
        return

    @property
    def texture_grain_size(self):
        """
        :return: Access to the Grain Size parameter in Texture Warp Mode.
        """
        return

    @property
    def tones_grain_size(self):
        """
        :return: Access to the Grain Size parameter in Tones Warp Mode.
        """
        return

    @property
    def warp_markers(self):
        """
        :return: Get the warp markers for this sample.
        """
        return

    @property
    def warp_mode(self):
        """
        :return: Access to the sample's warp mode.
        """
        return

    @property
    def warping(self) -> bool:
        """
        :return: Access to the sample's warping property.
        """
        return False

    def add_beats_granulation_resolution_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "beats_granulation_resolution" has changed.
        """
        return

    def add_beats_transient_envelope_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "beats_transient_envelope" has changed.
        """
        return

    def add_beats_transient_loop_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "beats_transient_loop_mode" has changed.
        """
        return

    def add_complex_pro_envelope_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "complex_pro_envelope" has changed.
        """
        return

    def add_complex_pro_formants_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "complex_pro_formants" has changed.
        """
        return

    def add_end_marker_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "end_marker" has changed.
        """
        return

    def add_file_path_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "file_path" has changed.
        """
        return

    def add_gain_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "gain" has changed.
        """
        return

    def add_slices_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "slices" has changed.
        """
        return

    def add_slicing_beat_division_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "slicing_beat_division" has changed.
        """
        return

    def add_slicing_region_count_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "slicing_region_count" has changed.
        """
        return

    def add_slicing_sensitivity_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "slicing_sensitivity" has changed.
        """
        return

    def add_slicing_style_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "slicing_style" has changed.
        """
        return

    def add_start_marker_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "start_marker" has changed.
        """
        return

    def add_texture_flux_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "texture_flux" has changed.
        """
        return

    def add_texture_grain_size_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "texture_grain_size" has changed.
        """
        return

    def add_tones_grain_size_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "tones_grain_size" has changed.
        """
        return

    def add_warp_markers_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "warp_markers" has changed.
        """
        return

    def add_warp_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "warp_mode" has changed.
        """
        return

    def add_warping_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "warping" has changed.
        """
        return

    def beat_to_sample_time(self, beat_time: float) -> float:
        """
        Converts the given beat time to sample time. Raises an error if the sample is not warped.
        """
        return 0.0

    def beats_granulation_resolution_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "beats_granulation_resolution".
        """
        return False

    def beats_transient_envelope_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "beats_transient_envelope".
        """
        return False

    def beats_transient_loop_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "beats_transient_loop_mode".
        """
        return False

    def clear_slices(self):
        """
        Clears all slices created in Simpler's manual mode.
        """
        return

    def complex_pro_envelope_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "complex_pro_envelope".
        """
        return False

    def complex_pro_formants_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "complex_pro_formants".
        """
        return False

    def end_marker_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "end_marker".
        """
        return False

    def file_path_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "file_path".
        """
        return False

    def gain_display_string(self) -> str:
        """
        Get the gain's display value as a string.
        """
        return ""

    def gain_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "gain".
        """
        return False

    def insert_slice(self, slice_time: int):
        """
        Add a slice point at the provided time if there is none.
        """
        return

    def move_slice(self, old_time: int, new_time: int) -> int:
        """
        Move the slice point at the provided time.
        """
        return 0

    def remove_beats_granulation_resolution_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "beats_granulation_resolution".
        """
        return

    def remove_beats_transient_envelope_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "beats_transient_envelope".
        """
        return

    def remove_beats_transient_loop_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "beats_transient_loop_mode".
        """
        return

    def remove_complex_pro_envelope_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "complex_pro_envelope".
        """
        return

    def remove_complex_pro_formants_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "complex_pro_formants".
        """
        return

    def remove_end_marker_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "end_marker".
        """
        return

    def remove_file_path_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "file_path".
        """
        return

    def remove_gain_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "gain".
        """
        return

    def remove_slice(self, slice_time: int):
        """
        Remove the slice point at the provided time if there is one.
        """
        return

    def remove_slices_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "slices".
        """
        return

    def remove_slicing_beat_division_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "slicing_beat_division".
        """
        return

    def remove_slicing_region_count_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "slicing_region_count".
        """
        return

    def remove_slicing_sensitivity_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "slicing_sensitivity".
        """
        return

    def remove_slicing_style_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "slicing_style".
        """
        return

    def remove_start_marker_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "start_marker".
        """
        return

    def remove_texture_flux_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "texture_flux".
        """
        return

    def remove_texture_grain_size_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "texture_grain_size".
        """
        return

    def remove_tones_grain_size_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "tones_grain_size".
        """
        return

    def remove_warp_markers_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "warp_markers".
        """
        return

    def remove_warp_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "warp_mode".
        """
        return

    def remove_warping_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "warping".
        """
        return

    def reset_slices(self):
        """
        Resets all edited slices to their original positions.
        """
        return

    def sample_to_beat_time(self, sample_time: float) -> float:
        """
        Converts the given sample time to beat time. Raises an error if the sample is not warped.
        """
        return 0.0

    def slices_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "slices".
        """
        return False

    def slicing_beat_division_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "slicing_beat_division".
        """
        return False

    def slicing_region_count_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "slicing_region_count".
        """
        return False

    def slicing_sensitivity_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "slicing_sensitivity".
        """
        return False

    def slicing_style_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "slicing_style".
        """
        return False

    def start_marker_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "start_marker".
        """
        return False

    def texture_flux_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "texture_flux".
        """
        return False

    def texture_grain_size_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "texture_grain_size".
        """
        return False

    def tones_grain_size_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "tones_grain_size".
        """
        return False

    def warp_markers_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "warp_markers".
        """
        return False

    def warp_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "warp_mode".
        """
        return False

    def warping_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "warping".
        """
        return False
