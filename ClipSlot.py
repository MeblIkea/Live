# All referenced (missing descriptions)
from typing import Optional, Callable
from Clip import Clip


class ClipShotPlayingState:
    recording = None
    started = None
    stopped = None


class ClipSlot:
    """
    This class represents an entry in Lives Session view matrix.
    """

    @property
    def _live_ptr(self) -> int:
        """
        :return: The pointer to the Live object.
        """
        return 0

    @property
    def canonical_parent(self):
        """
        Get the canonical parent of the ClipSlot.
        """
        return None

    @property
    def clip(self) -> Optional[Clip]:
        """
        Returns the Clip which this clip slots currently owns. Might be None.
        """
        return Clip()

    @property
    def color(self) -> int:
        """
        Returns the canonical color for the clip slot or None if it does not exist.
        """
        return 0

    @property
    def color_index(self) -> int:
        """
        Returns the canonical color index for the clip slot or None if it does not exist.
        """
        return 0

    @property
    def controls_other_clips(self) -> bool:
        """
        Returns true if firing this slot will fire clips in other slots.Can only be true for slots in group tracks.
        """
        return False

    @property
    def has_clip(self) -> bool:
        """
        Returns true if this Clipslot owns a Clip.
        """
        return False

    @property
    def has_stop_button(self) -> bool:
        """
        Get/Set if this Clip has a stop button, which will, if fired, stop any other Clip that is currently playing the Track we do belong to.
        """
        return False

    @property
    def is_group_slot(self) -> bool:
        """
        Returns whether this clip slot is a group track slot (group slot).
        """
        return False

    @property
    def is_playing(self) -> bool:
        """
        Returns whether the clip associated with the slot is playing.
        """
        return False

    @property
    def is_recording(self) -> bool:
        """
        Returns whether the clip associated with the slot is recording.
        """
        return False

    @property
    def is_triggered(self) -> bool:
        """
        Const access to the triggering state of the clip slot.
        """
        return False

    @property
    def playing_status(self) -> ClipShotPlayingState:
        """
        Const access to the playing state of the clip slot.Can be either stopped, playing, or recording.
        """
        return ClipShotPlayingState()

    @property
    def will_record_on_start(self) -> bool:
        """
        Returns true if the clip slot will record on being fired.
        """
        return False

    def add_color_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        return

    def add_color_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        return

    def add_controls_other_clips_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "controls_other_clips" has changed.
        """
        return

    def add_has_clip_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_clip" has changed.
        """
        return

    def add_has_stop_button_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_stop_button" has changed.
        """
        return

    def add_is_triggered_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "is_triggered" has changed.
        """
        return

    def add_playing_status_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "playing_status" has changed.
        """
        return

    def color_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color".
        """
        return False

    def color_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color_index".
        """
        return False

    def controls_other_clips_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "controls_other_clips".
        """
        return False

    def create_clip(self, arg2: float):
        """
        Creates an empty clip with the given length in the slot. Throws an error when called on non-empty slots or slots in non-MIDI tracks.
        """
        return

    def delete_clip(self):
        """
        Removes the clip contained in the slot. Raises an exception if the slot was empty.
        """
        return

    def duplicate_clip_to(self, arg2: 'ClipSlot'):
        """
        Duplicates the slot's clip to the passed in target slot. Overrides the target's clip if it's not empty. Raises an exception if the (source) slot itself is empty, or if source and target have different track types (audio vs. MIDI). Also raises if the source or target slot is in a group track (so called group slot).
        """
        return

    def fire(self, record_length: float = 1.7976931348623157e+308, launch_quantization: int = -2147483648,
             force_legato: bool = False):
        """
        If 'record_length' is passed, the clip will be refired after the given recording length.
        Raises an error if the slot owns a clip.
        'launch_quantization' determines the quantization of global transport that is applied overriding the value in the song.
        'force_legato' will make the clip play inmediatelly.
        The playhead will be moved to keep the clip synchronized.
        """
        return

    def has_clip_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_clip".
        """
        return False

    def has_stop_button_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_stop_button".
        """
        return False

    def is_triggered_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_triggered".
        """
        return False

    def playing_status_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "playing_status".
        """
        return False

    def remove_color_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "color_index".
        """
        return

    def remove_color_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "color".
        """
        return

    def remove_controls_other_clips_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "controls_other_clips".
        """
        return

    def remove_has_clip_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_clip".
        """
        return

    def remove_has_stop_button_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_stop_button".
        """
        return

    def remove_is_triggered_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_triggered".
        """
        return

    def remove_playing_status_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playing_status".
        """
        return

    def set_fire_button_state(self, arg2: bool):
        """
        Set the clip slot's fire button state directly. Supports all launch modes.
        """
        return

    def stop(self):
        """
        Stop playing the contained Clip, if there is a Clip and it's currently playing.
        """
        return
