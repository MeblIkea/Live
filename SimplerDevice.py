# Have to do simpledevice.view
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
