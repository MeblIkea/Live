# All referenced (missing descriptions)
from typing import Any, Callable
from Live.Base import Vector
from Live.Device import Device
from Live.GroovePool import GroovePool
from Live.Scene import Scene
from Live.Track import Track


def get_all_scales_ordered() -> tuple:
    """
    Get an ordered tuple of tuples of all available scale names to intervals.
    """
    return ()


class BeatTime:
    """
    Represents a Time, splitted into Bars, Beats, SubDivision and Ticks.
    """

    @property
    def bars(self) -> int:
        """
        Get the number of Bars.
        """
        return 0

    @property
    def beats(self) -> int:
        """
        Get the number of Beats.
        """
        return 0

    @property
    def sub_division(self) -> int:
        """
        Get the number of SubDivisions.
        """
        return 0

    @property
    def ticks(self) -> int:
        """
        Get the number of Ticks.
        """
        return 0


class CaptureDestination:
    """
    The destination for MIDI capture.
    """
    arrangement = None
    auto = None
    session = None


class CaptureMode:
    """
    The mode for capturing clips.
    """
    all = None
    all_except_selected = None


class CuePoint:
    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0

    @property
    def canonical_parent(self):
        """
        Get the canonical parent of the Cue Point.
        """
        return

    @property
    def name(self) -> str:
        """
        Get/Listen to the name of the Cue Point.
        """
        return ''

    @property
    def time(self) -> float:
        """
        Get/Listen to the Cue Point's time in beats.
        """
        return 0.0

    def add_name_listener(self, arg2: Any) -> None:
        """
        Add a listener to when the property "name" changes.
        """
        return

    def add_time_listener(self, arg2: Any) -> None:
        """
        Add a listener to when the property "time" changes.
        """
        return

    def jump(self) -> None:
        """
        When the Song is playing, set the playing-position quantized to this Cue point's time.
        When not playing, simply move the start playing position.
        """

    def name_has_listener(self, arg2: Any) -> bool:
        """
        Check if a listener is registered to the property "name"
        """
        return False

    def remove_name_listener(self, arg2: Any) -> None:
        """
        Remove a listener from the property "name"
        """
        return

    def remove_time_listener(self, arg2: Any) -> None:
        """
        Remove a listener from the property "time"
        """
        return

    def time_has_listener(self, arg2: Any) -> bool:
        """
        Check if a listener is registered to the property "time"
        """
        return False


class Quantization:
    q_2_bars = None
    q_4_bars = None
    q_8_bars = None
    q_bar = None
    q_eight = None
    q_eight_triplet = None
    q_half = None
    q_half_triplet = None
    q_no_q = None
    q_quarter = None
    q_quarter_triplet = None
    q_sixteenth = None
    q_sixteenth_triplet = None
    q_thirtyworth = None


class RecordingQuantization:
    rec_q_eight = None
    rec_q_eight_eight_triplet = None
    rec_q_eight_triplet = None
    req_q_no_q = None
    rec_q_quarter = None
    req_q_sixteenth = None
    req_q_sixteenth_sixteenth_triplet = None
    rec_q_sixteenth_triplet = None
    rec_q_thirtysecond = None


class SessionRecordStatus:
    off = None
    on = None
    transition = None


class SmptTime:
    frames = None
    hours = None
    minutes = None
    seconds = None


class Song:
    class View:
        @property
        def _live_ptr(self) -> int:
            """
            Get the pointer to the Live Object.
            """
            return 0

        @property
        def canonical_parent(self):
            """
            Get the canonical parent of the song view.
            """
            return

        @property
        def detail_clip(self):
            """
            Get/Set the Clip that is currently visible in Live's Detail view.
            """
            return

        @property
        def draw_mode(self) -> bool:
            """
            Get/Set if the Envelope/Note draw mode is enabled.
            """
            return False

        @property
        def follow_song(self) -> bool:
            """
            Get/Set if the Arrangement view should scroll to show the play marker.
            """
            return False

        @property
        def highlighted_clip_slot(self):
            """
            Get/Set the clip slot, defined via the highlighted track and scene in the Session. Will be None for Master and Send tracks.
            """
            return

        @property
        def selected_chain(self):
            """
            Get the highlighted chain if available.
            """
            return

        @property
        def selected_parameter(self):
            """
            Get the currently selected device parameter.
            """
            return

        @property
        def selected_scene(self) -> Scene:
            """
            Get/Set the currently selected scene in Live's Session view.
            """
            return Scene()

        @property
        def selected_track(self) -> Track:
            """
            Get/Set the currently selected Track in Live's Session or Arrangement view.
            """
            return Track()

        def add_detail_clip_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "detail_clip" changes.
            """
            return

        def add_draw_mode_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "draw_mode" changes.
            """
            return

        def add_follow_song_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "follow_song" changes.
            """
            return

        def add_selected_chain_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_chain" changes.
            """
            return

        def add_selected_parameter_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_parameter" changes.
            """
            return

        def add_selected_scene_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_scene" changes.
            """
            return

        def add_selected_track_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_track" changes.
            """
            return

        def detail_clip_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "detail_clip"
            """
            return False

        def draw_mode_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "draw_mode"
            """
            return False

        def follow_song_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "follow_song"
            """
            return False

        def remove_detail_clip_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "detail_clip"
            """
            return

        def remove_draw_mode_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "draw_mode"
            """
            return

        def remove_follow_song_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "follow_song"
            """
            return

        def remove_selected_chain_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_chain"
            """
            return

        def remove_selected_parameter_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_parameter"
            """
            return

        def remove_selected_scene_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_scene"
            """
            return

        def remove_selected_track_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_track"
            """
            return

        def select_device(self, arg2: Device, ShouldAppointDevice: bool = True) -> None:
            """
            Select the given device.
            """
            return

        def selected_chain_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_chain"
            """
            return False

        def selected_parameter_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_parameter"
            """
            return False

        def selected_scene_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_scene"
            """
            return False

        def selected_track_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_track"
            """
            return False

    @property
    def _live_ptr(self) -> int:
        """
        :return: The pointer to the Live object.
        """
        return 0

    @property
    def appointed_device(self) -> 'Device':
        """
        Read, write and listen access to the currently appointed device.
        """
        return Device()

    @property
    def arrangement_overdub(self) -> bool:
        """
        Get/Set the global arrangement overdub state.
        """
        return False

    @property
    def back_to_arranger(self) -> bool:
        """
        Get/Set if triggering a Clip in the Session, disabled the playback of Clips in the Arranger.
        """
        return False

    @property
    def can_capture_midi(self) -> bool:
        """
        Get whether there currently is material to be captured on any tracks.
        """
        return False

    @property
    def can_jump_to_next_cue(self) -> bool:
        """
        Get whether it is possible to jump to the next cue.
        """
        return False

    @property
    def can_jump_to_prev_cue(self) -> bool:
        """
        Get whether it is possible to jump to the previous cue.
        """
        return False

    @property
    def can_redo(self) -> bool:
        """
        Get whether it is possible to redo the last action.
        """
        return False

    @property
    def can_undo(self) -> bool:
        """
        Get whether it is possible to undo the last action.
        """
        return False

    @property
    def canonical_parent(self):
        """
        Get the canonical parent of the object.
        """
        return None

    @property
    def clip_trigger_quantization(self) -> int:
        """
        Get/Set the global Clip trigger quantization.
        """
        return 0

    @property
    def count_in_duration(self) -> int:
        """
        Get the count in duration. Returns an index, mapped as follows: 0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.
        """
        return 0

    @property
    def cue_points(self) -> Vector:
        """
        Get the cue points in the song.
        """
        return Vector()

    @property
    def current_song_time(self) -> float:
        """
        Get the current song time in beats.
        """
        return 0.0

    @property
    def exclusive_arm(self) -> bool:
        """
        Get if Tracks should be armed exclusively by default.
        """
        return False

    @property
    def exclusive_solo(self) -> bool:
        """
        Get if Tracks should be soloed exclusively by default.
        """
        return False

    @property
    def groove_amount(self) -> float:
        """
        Get/Set the global groove amount.
        """
        return 0.0

    @property
    def groove_pool(self) -> 'GroovePool':
        """
        Get the groove pool.
        """
        return GroovePool()

    @property
    def is_counting_in(self) -> bool:
        """
        Get whether the song is currently counting in.
        """
        return False

    @property
    def is_playing(self) -> bool:
        """
        Get whether the song is currently playing.
        """
        return False

    @property
    def last_event_time(self) -> float:
        """
        Get the time of the last event.
        """
        return 0.0

    @property
    def loop(self) -> bool:
        """
        Get/Set the looping flag that en/disables the usage of the globalloop markers in the song.
        """
        return False

    @property
    def loop_length(self) -> float:
        """
        Get/Set the length of the global loop marker position in beats.
        """
        return 0.0

    @property
    def loop_start(self) -> float:
        """
        Get/Set the start of the global loop marker position in beats.
        """
        return 0.0

    @property
    def master_track(self) -> 'Track':
        """
        Get the master track.
        """
        return Track()

    @property
    def metronome(self) -> bool:
        """
        Get/Set the metronome state.
        """
        return False

    @property
    def midi_recording_quantization(self) -> int:
        """
        Get/Set the global MIDI recording quantization.
        """
        return 0

    @property
    def nudge_down(self) -> bool:
        """
        Get/Set the nudge down state.
        """
        return False

    @property
    def nudge_up(self) -> bool:
        """
        Get/Set the nudge up state.
        """
        return False

    @property
    def overdub(self) -> bool:
        """
        Legacy hook for Live 8 overdub state. Now hooks to session record, but never starts playback.
        """
        return False

    @property
    def punch_in(self) -> bool:
        """
        Get/Set the global punch in state.
        """
        return False

    @property
    def punch_out(self) -> bool:
        """
        Get/Set the global punch out state.
        """
        return False

    @property
    def re_enable_automation_enabled(self) -> bool:
        """
        Get/Set the re-enable automation state.
        """
        return False

    @property
    def record_mode(self) -> int:
        """
        Get/Set the record mode.
        """
        return 0

    @property
    def return_tracks(self) -> Vector[Track]:
        """
        Get the return tracks.
        """
        return Vector()

    @property
    def root_note(self) -> int:
        """
        Set and access the root note (i.e. key) of the song used for control surfaces. The root note can be a number between 0 and 11, with 0 corresponding to C and 11 corresponding to B.
        """
        return 0

    @property
    def scale_intervals(self) -> list[int]:
        """
        Reports the current scale's intervals as a list of integers, starting with the root note and representing the number of half steps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)
        """
        return []

    @property
    def scale_name(self) -> str:
        """
        Reports the current scale's name.
        """
        return ''

    @property
    def scenes(self) -> Vector[Scene]:
        """
        Get the scenes.
        """
        return Vector()

    @property
    def select_on_launch(self) -> bool:
        """
        Get if Scenes and Clips should be selected when fired.
        """
        return False

    @property
    def session_automation_record(self) -> bool:
        """
        Get the session automation record state.
        """
        return False

    @property
    def session_record(self) -> bool:
        """
        Get the session record state.
        """
        return False

    @property
    def session_record_status(self) -> int:
        """
        Get the session slot-recording state.
        """
        return 0

    @property
    def signature_denominator(self) -> int:
        """
        Get/Set the global time signature denominator.
        """
        return 0

    @property
    def signature_numerator(self) -> int:
        """
        Get/Set the global time signature numerator.
        """
        return 0

    @property
    def song_length(self) -> float:
        """
        Get the song length in beats.
        """
        return 0.0

    @property
    def swing_amount(self) -> float:
        """
        Get/Set the global swing amount.
        """
        return 0.0

    @property
    def tempo(self) -> float:
        """
        Get/Set the global tempo.
        """
        return 0.0

    @property
    def tracks(self) -> Vector[Track]:
        """
        Get the tracks.
        """
        return Vector()

    @property
    def view(self) -> 'Song.View':
        """
        Get the view object.
        """
        return Song.View()

    @property
    def visible_tracks(self) -> Vector[Track]:
        """
        Get the visible tracks.
        """
        return Vector()

    def add_appointed_device_listener(self, arg2: Callable):
        """
        Add a listener to the property "appointed_device". The listener is called when the appointed device changes.
        """
        return

    def add_arrangement_overdub_listener(self, arg2: Callable):
        """
        Add a listener to the property "arrangement_overdub". The listener is called when the arrangement overdub status changes.
        """
        return

    def add_back_to_arranger_listener(self, arg2: Callable):
        """
        Add a listener to the property "back_to_arranger". The listener is called when the back to arrangement status changes.
        """
        return

    def add_can_capture_midi_listener(self, arg2: Callable):
        """
        Add a listener to the property "can_capture_midi". The listener is called when the capture midi status changes.
        """
        return

    def add_can_jump_to_next_cue_listener(self, arg2: Callable):
        """
        Add a listener to the property "can_jump_to_next_cue". The listener is called when the can jump to next cue status changes.
        """
        return

    def add_can_jump_to_prev_cue_listener(self, arg2: Callable):
        """
        Add a listener to the property "can_jump_to_prev_cue". The listener is called when the can jump to previous cue status changes.
        """
        return

    def add_clip_trigger_quantization_listener(self, arg2: Callable):
        """
        Add a listener to the property "clip_trigger_quantization". The listener is called when the clip trigger quantization changes.
        """
        return

    def add_count_in_duration_listener(self, arg2: Callable):
        """
        Add a listener to the property "count_in_duration". The listener is called when the count in duration changes.
        """
        return

    def add_cue_points_listener(self, arg2: Callable):
        """
        Add a listener to the property "cue_points". The listener is called when the cue points change.
        """
        return

    def add_current_song_time_listener(self, arg2: Callable):
        """
        Add a listener to the property "current_song_time". The listener is called when the current song time changes.
        """
        return

    def add_data_listener(self, arg2: Callable):
        """
        Add a listener to the property "data". The listener is called when the data changes.
        """
        return

    def add_exclusive_arm_listener(self, arg2: Callable):
        """
        Add a listener to the property "exclusive_arm". The listener is called when the exclusive arm status changes.
        """
        return

    def add_groove_amount_listener(self, arg2: Callable):
        """
        Add a listener to the property "groove_amount". The listener is called when the groove amount changes.
        """
        return

    def add_is_counting_in_listener(self, arg2: Callable):
        """
        Add a listener to the property "is_counting_in". The listener is called when the count in status changes.
        """
        return

    def add_is_playing_listener(self, arg2: Callable):
        """
        Add a listener to the property "is_playing". The listener is called when the playing status changes.
        """
        return

    def add_loop_length_listener(self, arg2: Callable):
        """
        Add a listener to the property "loop_length". The listener is called when the loop length changes.
        """
        return

    def add_loop_listener(self, arg2: Callable):
        """
        Add a listener to the property "loop". The listener is called when the loop status changes.
        """
        return

    def add_loop_start_listener(self, arg2: Callable):
        """
        Add a listener to the property "loop_start". The listener is called when the loop start changes.
        """
        return

    def add_metronome_listener(self, arg2: Callable):
        """
        Add a listener to the property "metronome". The listener is called when the metronome status changes.
        """
        return

    def add_midi_recording_quantization_listener(self, arg2: Callable):
        """
        Add a listener to the property "midi_recording_quantization". The listener is called when the midi recording quantization changes.
        """
        return

    def add_nudge_down_listener(self, arg2: Callable):
        """
        Add a listener to the property "nudge_down". The listener is called when the nudge down status changes.
        """
        return

    def add_nudge_up_listener(self, arg2: Callable):
        """
        Add a listener to the property "nudge_up". The listener is called when the nudge up status changes.
        """
        return

    def add_overdub_listener(self, arg2: Callable):
        """
        Add a listener to the property "overdub". The listener is called when the overdub status changes.
        """
        return

    def add_punch_in_listener(self, arg2: Callable):
        """
        Add a listener to the property "punch_in". The listener is called when the punch in status changes.
        """
        return

    def add_punch_out_listener(self, arg2: Callable):
        """
        Add a listener to the property "punch_out". The listener is called when the punch out status changes.
        """
        return

    def add_re_enable_automation_enabled_listener(self, arg2: Callable):
        """
        Add a listener to the property "re_enable_automation_enabled". The listener is called when the re enable automation status changes.
        """
        return

    def add_record_mode_listener(self, arg2: Callable):
        """
        Add a listener to the property "record_mode". The listener is called when the record mode changes.
        """
        return

    def add_return_tracks_listener(self, arg2: Callable):
        """
        Add a listener to the property "return_tracks". The listener is called when the return tracks change.
        """
        return

    def add_root_note_listener(self, arg2: Callable):
        """
        Add a listener to the property "root_note". The listener is called when the root note changes.
        """
        return

    def add_scale_intervals_listener(self, arg2: Callable):
        """
        Add a listener to the property "scale_intervals". The listener is called when the scale intervals change.
        """
        return

    def add_scale_name_listener(self, arg2: Callable):
        """
        Add a listener to the property "scale_name". The listener is called when the scale name changes.
        """
        return

    def add_scenes_listener(self, arg2: Callable):
        """
        Add a listener to the property "scenes". The listener is called when the scenes change.
        """
        return

    def add_session_automation_record_listener(self, arg2: Callable):
        """
        Add a listener to the property "session_automation_record". The listener is called when the session automation record status changes.
        """
        return

    def add_session_record_listener(self, arg2: Callable):
        """
        Add a listener to the property "session_record". The listener is called when the session record status changes.
        """
        return

    def add_session_record_status_listener(self, arg2: Callable):
        """
        Add a listener to the property "session_record_status". The listener is called when the session record status changes.
        """
        return

    def add_signature_denominator_listener(self, arg2: Callable):
        """
        Add a listener to the property "signature_denominator". The listener is called when the signature denominator changes.
        """
        return

    def add_signature_numerator_listener(self, arg2: Callable):
        """
        Add a listener to the property "signature_numerator". The listener is called when the signature numerator changes.
        """
        return

    def add_song_length_listener(self, arg2: Callable):
        """
        Add a listener to the property "song_length". The listener is called when the song length changes.
        """
        return

    def add_swing_amount_listener(self, arg2: Callable):
        """
        Add a listener to the property "swing_amount". The listener is called when the swing amount changes.
        """
        return

    def add_tempo_listener(self, arg2: Callable):
        """
        Add a listener to the property "tempo". The listener is called when the tempo changes.
        """
        return

    def add_tracks_listener(self, arg2: Callable):
        """
        Add a listener to the property "tracks". The listener is called when the tracks change.
        """
        return

    def add_visible_tracks_listener(self, arg2: Callable):
        """
        Add a listener to the property "visible_tracks". The listener is called when the visible tracks change.
        """
        return

    def appointed_device_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "appointed_device".
        """
        return False

    def arrangement_overdub_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "arrangement_overdub".
        """
        return False

    def back_to_arranger_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "back_to_arranger".
        """
        return False

    def can_capture_midi_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "can_capture_midi".
        """
        return False

    def can_jump_to_next_cue_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "can_jump_to_next_cue".
        """
        return False

    def can_jump_to_prev_cue_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "can_jump_to_prev_cue".
        """
        return False

    def capture_midi(self, destination: int = CaptureMode.all):
        """
        Capture the current MIDI input.
        """
        return

    def clip_trigger_quantization_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "clip_trigger_quantization".
        """
        return False

    def continue_playing(self):
        """
        Continue playing the song from the current position.
        """
        return

    def count_in_duration_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "count_in_duration".
        """
        return False

    def create_audio_track(self, index: int = None) -> Track:
        """
        Create a new audio track at the given index.
        """
        return Track()

    def create_midi_track(self, index: int = None) -> Track:
        """
        Create a new MIDI track at the given index.
        """
        return Track()

    def create_return_track(self) -> Track:
        """
        Create a new return track.
        """
        return Track()

    def create_scene(self, arg2: int) -> Scene:
        """
        Create a new scene at the given index.
        """
        return Scene

    def cue_points_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "cue_points".
        """
        return False

    def current_song_time_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "current_song_time".
        """
        return False

    def data_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "data".
        """
        return False

    def delete_return_track(self, arg2: Track):
        """
        Delete the given return track.
        """
        return

    def delete_scene(self, arg2: Scene):
        """
        Delete the given scene.
        """
        return

    def delete_track(self, arg2: Track):
        """
        Delete the given track.
        """
        return

    def duplicate_scene(self, arg2: Scene):
        """
        Duplicate the given scene.
        """
        return

    def duplicate_track(self, arg2: Track):
        """
        Duplicate the given track.
        """
        return

    def end_undo_step(self):
        """
        End the current undo step.
        """
        return

    def exclusive_arm_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "exclusive_arm".
        """
        return False

    def find_device(self, device: Device, target, target_position: int) -> int:
        """
        Returns the closest possible position to the given target, where the device can be inserted.
        If inserting is not possible at all (i.e. if the device type is wrong), -1 is returned.
        """
        return 0

    def force_link_beat_time(self):
        """
        Force the Link timeline to jump to Lives current beat time. Danger: This can cause beat time discontinuities in other connected apps.
        """
        return

    def get_beats_loop_length(self) -> BeatTime:
        """
        Get const access to the songs loop length, using a BeatTime class with the current global set signature.
        """
        return BeatTime()

    def get_beats_loop_start(self) -> BeatTime:
        """
        Get const access to the songs loop start, using a BeatTime class with the current global set signature.
        """
        return BeatTime()

    def get_current_beats_song_time(self) -> BeatTime:
        """
        Get const access to the songs current time, using a BeatTime class with the current global set signature.
        """
        return BeatTime()

    def get_current_smpte_song_time(self, arg2: int) -> SmptTime:
        """
        Get const access to the songs current playing position, by specifying the SMPTE format in which you would like to receive the time.
        """
        return SmptTime()

    def get_data(self, arg2) -> bool:
        """
        Get data for the given key, that was previously stored using set_data.
        """
        return False

    def groove_amount_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "groove_amount".
        """
        return False

    def is_counting_in_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_counting_in".
        """
        return False

    def is_cue_point_selected(self) -> bool:
        """
        Returns true, if a cue point is selected.
        """
        return False

    def is_playing_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_playing".
        """
        return False

    def jump_by(self, arg2: float):
        """
        Set a new playing pos, relative to the current one.
        """
        return

    def jump_to_next_cue(self):
        """
        Jump to the next cue point.
        """
        return

    def jump_to_prev_cue(self):
        """
        Jump to the previous cue point.
        """
        return

    def loop_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "loop".
        """
        return False

    def loop_length_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "loop_length".
        """
        return False

    def loop_start_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "loop_start".
        """
        return False

    def metronome_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "metronome".
        """
        return False

    def midi_recording_quantization_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "midi_recording_quantization".
        """
        return False

    def move_device(self, device: Device, target, target_position: int) -> int:
        """
        Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.
        If the device cannot be moved to this position, the nearest possible position is chosen.
        If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to.
        """
        return 0

    def nudge_down_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "nudge_down".
        """
        return False

    def nudge_up_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "nudge_up".
        """
        return False

    def overdub_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "overdub".
        """
        return False

    def play_selection(self):
        """
        Start playing the current set selection, or do nothing if no selection is set.
        """
        return

    def punch_in_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "punch_in".
        """
        return False

    def punch_out_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "punch_out".
        """
        return False

    def re_enable_automation(self):
        """
        Discards overrides of automated parameters.
        """
        return

    def re_enable_automation_enabled_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "re_enable_automation_enabled".
        """
        return False

    def record_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "record_mode".
        """
        return False

    def redo(self):
        """
        Redo the last action that was undone.
        """
        return

    def remove_appointed_device_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "appointed_device".
        """
        return

    def remove_arrangement_overdub_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "arrangement_overdub".
        """
        return

    def remove_back_to_arranger_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "back_to_arranger".
        """
        return

    def remove_can_capture_midi_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "can_capture_midi".
        """
        return

    def remove_can_jump_to_next_cue_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "can_jump_to_next_cue".
        """
        return

    def remove_can_jump_to_prev_cue_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "can_jump_to_prev_cue".
        """
        return

    def remove_clip_trigger_quantization_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "clip_trigger_quantization".
        """
        return

    def remove_count_in_duration_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "count_in_duration".
        """
        return

    def remove_cue_points_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "cue_points".
        """
        return

    def remove_current_song_time_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "current_song_time".
        """
        return

    def remove_data_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "data".
        """
        return

    def remove_exclusive_arm_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "exclusive_arm".
        """
        return

    def remove_groove_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "groove_amount".
        """
        return

    def remove_is_counting_in_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_counting_in".
        """
        return

    def remove_is_playing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_playing".
        """
        return

    def remove_loop_length_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "loop_length".
        """
        return

    def remove_loop_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "loop".
        """
        return

    def remove_loop_start_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "loop_start".
        """
        return

    def remove_metronome_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "metronome".
        """
        return

    def remove_midi_recording_quantization_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "midi_recording_quantization".
        """
        return

    def remove_nudge_down_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "nudge_down".
        """
        return

    def remove_nudge_up_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "nudge_up".
        """
        return

    def remove_overdub_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "overdub".
        """
        return

    def remove_punch_in_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "punch_in".
        """
        return

    def remove_punch_out_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "punch_out".
        """
        return

    def remove_re_enable_automation_enabled_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "re_enable_automation_enabled".
        """
        return

    def remove_record_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "record_mode".
        """
        return

    def remove_return_tracks_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "return_tracks".
        """
        return

    def remove_root_note_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "root_note".
        """
        return

    def remove_scale_intervals_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "scale_intervals".
        """
        return

    def remove_scale_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "scale_name".
        """
        return

    def remove_scenes_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "scenes".
        """
        return

    def remove_session_automation_record_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "session_automation_record".
        """
        return

    def remove_session_record_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "session_record".
        """
        return

    def remove_session_record_status_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "session_record_status".
        """
        return

    def remove_signature_denominator_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "signature_denominator".
        """
        return

    def remove_signature_numerator_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "signature_numerator".
        """
        return

    def remove_song_length_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "song_length".
        """
        return

    def remove_swing_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "swing_amount".
        """
        return

    def remove_tempo_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "tempo".
        """
        return

    def remove_tracks_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "tracks".
        """
        return

    def remove_visible_tracks_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "visible_tracks".
        """
        return

    def return_tracks_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "return_tracks".
        """
        return False

    def root_note_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "root_note".
        """
        return False

    def scale_intervals_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "scale_intervals".
        """
        return False

    def scale_name_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "scale_name".
        """
        return False

    def scenes_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "scenes".
        """
        return False

    def scrub_by(self, arg2: float):
        """
        Same as jump_by, but does not stop playback.
        """
        return

    def session_automation_record_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "session_automation_record".
        """
        return False

    def session_record_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "session_record".
        """
        return False

    def session_record_status_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "session_record_status".
        """
        return False

    def set_data(self, key, value):
        """
        Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
        """
        return

    def set_or_delete_cue(self):
        """
        When a cue is selected, it gets deleted. If no cue is selected, a new cue is created at the current global songtime.
        """
        return

    def signature_denominator_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "signature_denominator".
        """
        return False

    def signature_numerator_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "signature_numerator".
        """
        return False

    def song_length_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "song_length".
        """
        return False

    def start_playing(self):
        """
        Start playing from the startmarker.
        """
        return

    def stop_all_clips(self, quantized: bool = True):
        """
        Stop all playing Clips (if any) but continue playing the Song.
        """
        return

    def stop_playing(self):
        """
        Stop playing the Song.
        """
        return

    def swing_amount_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "swing_amount".
        """
        return False

    def tap_tempo(self):
        """
        Trigger the tap tempo function.
        """
        return

    def tempo_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "tempo".
        """
        return False

    def tracks_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "tracks".
        """
        return False

    def trigger_session_record(self, record_length: float = 1.7976931348623157e+308):
        """
        Triggers a new session recording.
        """
        return

    def undo(self):
        """
        Undo the last action that was made.
        """
        return

    def visible_tracks_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "visible_tracks".
        """
        return False


class TimeFormat:
    ms_time = 0
    smpte_24 = 0
    smpte_25 = 0
    smpte_29 = 0
    smpte_30 = 0
    smpte_30_drop = 0
