# All referenced (missing descriptions)
from typing import Callable
from Live.Base import IntVector
from Live.Device import Device


def get_available_voice_numbers() -> IntVector:
    """
    :return: Get the available voice numbers for this device.
    """
    return IntVector()


class PlaybackMode:
    classic = None
    one_shot = None
    slicing = None


class SlicingPlaybackMode:
    mono = None
    poly = None
    thru = None


class SimplerDevice(Device):
    """
    This class represents a Simpler device.
    """
    class View(Device.View):
        """
        Representing the view aspects of a simpler device.
        """
        @property
        def sample_end(self) -> int:
            """
            :return: Access to the modulated samples end position in samples.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def sample_env_fade_in(self) -> int:
            """
            :return: Access to the envelope fade-in time in samples.
            Returned value is only in use when Simpler is in one-shot mode.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def sample_env_fade_out(self) -> int:
            """
            :return: Access to the envelope fade-out time in samples.
            Returned value is only in use when Simpler is in one-shot mode.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def sample_loop_end(self) -> int:
            """
            :return: Access to the modulated samples loop end position in samples.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def sample_loop_fade(self) -> int:
            """
            :return: Access to the modulated samples loop fade position in samples.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def sample_loop_start(self) -> int:
            """
            :return: Access to the modulated samples loop start position in samples.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def sample_start(self) -> int:
            """
            :return: Access to the modulated samples start position in samples.
            Returns -1 in case there is no sample loaded.
            """
            return 0

        @property
        def selected_slice(self) -> int:
            """
            :return: Access to the selected slice.
            """
            return 0

        def add_sample_end_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_end" has changed.
            """
            return

        def add_sample_env_fade_in_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_env_fade_in" has changed.
            """
            return

        def add_sample_env_fade_out_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_env_fade_out" has changed.
            """
            return

        def add_sample_loop_end_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_loop_end" has changed.
            """
            return

        def add_sample_loop_fade_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_loop_fade" has changed.
            """
            return

        def add_sample_loop_start_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_loop_start" has changed.
            """
            return

        def add_sample_start_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "sample_start" has changed.
            """
            return

        def add_selected_slice_listener(self, arg2: Callable):
            """
            Add a listener function or method, which will be called as soon as the property "selected_slice" has changed.
            """
            return

        def remove_sample_end_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_end".
            """
            return

        def remove_sample_env_fade_in_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_env_fade_in".
            """
            return

        def remove_sample_env_fade_out_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_env_fade_out".
            """
            return

        def remove_sample_loop_end_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_loop_end".
            """
            return

        def remove_sample_loop_fade_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_loop_fade".
            """
            return

        def remove_sample_loop_start_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_loop_start".
            """
            return

        def remove_sample_start_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "sample_start".
            """
            return

        def remove_selected_slice_listener(self, arg2: Callable):
            """
            Remove a previously set listener function or method from property "selected_slice".
            """
            return

        def sample_end_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_end".
            """
            return False

        def sample_env_fade_in_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_env_fade_in".
            """
            return False

        def sample_env_fade_out_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_env_fade_out".
            """
            return False

        def sample_loop_end_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_loop_end".
            """
            return False

        def sample_loop_fade_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_loop_fade".
            """
            return False

        def sample_loop_start_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_loop_start".
            """
            return False

        def sample_start_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample_start".
            """
            return False

        def selected_slice_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_slice".
            """
            return False

    @property
    def can_warp_as(self) -> bool:
        """
        :return: Returns true if warp_as is available.
        """
        return False

    @property
    def can_warp_double(self) -> bool:
        """
        :return: Returns true if warp_double is available.
        """
        return False

    @property
    def can_warp_half(self) -> bool:
        """
        :return: Returns true if warp_half is available.
        """
        return False

    @property
    def multi_sample_mode(self) -> bool:
        """
        :return: Returns whether Simpler is in multi-sample mode.
        """
        return False

    @property
    def pad_slicing(self) -> bool:
        """
        :return: When set to true, slices can be added in slicing mode by playing notes that are not assigned to slices, yet.
        """
        return False

    @property
    def playback_mode(self) -> PlaybackMode:
        """
        :return: Access to Simpler's playback mode.
        """
        return PlaybackMode()

    @property
    def playing_position(self) -> float:
        """
        :return: Constant access to the current playing position in the sample.
        The returned value is the normalized position between sample start and end.
        """
        return 0.0

    @property
    def playing_position_enabled(self) -> bool:
        """
        :return: Returns whether Simpler is showing the playing position.
        The returned value is True while the sample is played back.
        """
        return False

    @property
    def retrigger(self) -> bool:
        """
        :return: Access to Simpler's retrigger mode.
        """
        return False

    @property
    def sample(self):
        """
        :return: Get the loaded Sample.
        """
        return

    @property
    def slicing_playback_mode(self) -> PlaybackMode:
        """
        :return: Access to Simpler's slicing playback mode.
        """
        return PlaybackMode()

    @property
    def voices(self) -> int:
        """
        :return: Access to the number of voices in Simpler.
        """
        return 0

    def add_can_warp_as_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "can_warp_as" has changed.
        """
        return

    def add_can_warp_double_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "can_warp_double" has changed.
        """
        return

    def add_can_warp_half_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "can_warp_half" has changed.
        """
        return

    def add_multi_sample_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "multi_sample_mode" has changed.
        """
        return

    def add_pad_slicing_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "pad_slicing" has changed.
        """
        return

    def add_playback_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "playback_mode" has changed.
        """
        return

    def add_playing_position_enabled_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "playing_position_enabled" has changed.
        """
        return

    def add_playing_position_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "playing_position" has changed.
        """
        return

    def add_retrigger_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "retrigger" has changed.
        """
        return

    def add_sample_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "sample" has changed.
        """
        return

    def add_slicing_playback_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "slicing_playback_mode" has changed.
        """
        return

    def add_voices_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "voices" has changed.
        """
        return

    def can_warp_as_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "can_warp_as".
        """
        return False

    def can_warp_double_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "can_warp_double".
        """
        return False

    def can_warp_half_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "can_warp_half".
        """
        return False

    def crop(self):
        """
        Crop the loaded sample to the active area between start- and end marker.
        Calling this method on an empty simpler raises an error.
        """
        return

    def guess_playback_length(self) -> float:
        """
        Return an estimated beat time for the playback length between start- and end-marker.
        Calling this method on an empty simpler raises an error.
        """
        return 0.0

    def remove_can_warp_as_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "can_warp_as".
        """
        return

    def remove_can_warp_double_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "can_warp_double".
        """
        return

    def remove_can_warp_half_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "can_warp_half".
        """
        return

    def remove_multi_sample_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "multi_sample_mode".
        """
        return

    def remove_pad_slicing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "pad_slicing".
        """
        return

    def remove_playback_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playback_mode".
        """
        return

    def remove_playing_position_enabled_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playing_position_enabled".
        """
        return

    def remove_playing_position_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playing_position".
        """
        return

    def remove_retrigger_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "retrigger".
        """
        return

    def remove_sample_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "sample".
        """
        return

    def remove_slicing_playback_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "slicing_playback_mode".
        """
        return

    def remove_voices_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "voices".
        """
        return

    def retrigger_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "retrigger".
        """
        return False

    def reverse(self):
        """
        Reverse the loaded sample.
        Calling this method on an empty simpler raises an error.
        """
        return

    def sample_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "sample".
        """
        return False

    def slicing_playback_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "slicing_playback_mode".
        """
        return False

    def voices_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "voices".
        """
        return False

    def warp_as(self, beat_time: float):
        """
        Warp the playback region between start- and end-marker as the given length.
        Calling this method on an empty simpler raises an error.
        """
        return

    def warp_double(self):
        """
        Doubles the tempo for region between start- and end-marker.
        """
        return

    def warp_half(self):
        """
        Halves the tempo for region between start- and end-marker.
        """
        return
