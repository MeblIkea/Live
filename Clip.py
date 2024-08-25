# All referenced (missing descriptions)
from typing import Callable
from Live.Base import Vector
from Live.DeviceParameter import DeviceParameter
from Live.Groove import Groove


class AutomationEnvelope:
    def insert_step(self, arg2: float, arg3: float, arg4: float):
        return

    def value_at_time(self, arg2: float):
        return 0.0


class ClipLaunchQuantization:
    q_2_barsValue = None
    q_4_barsValue = None
    q_8_barsValue = None
    q_barValue = None
    q_eighthValue = None
    q_eighth_tripletValue = None
    q_globalValue = None
    q_halfValue = None
    q_half_tripletValue = None
    q_noneValue = None
    q_quarterValue = None
    q_quarter_tripletValue = None
    q_sixteenthValue = None
    q_sixteenth_tripletValue = None
    q_thirtysecondValue = None


class GridQuantization:
    countValue = None
    g_2_barsValue = None
    g_4_barsValue = None
    g_8_barsValue = None
    g_barValue = None
    g_eighthValue = None
    g_halfValue = None
    g_quarterValue = None
    g_sixteenthValue = None
    g_thirtysecondValue = None
    no_gridValue = None


class LaunchMode:
    gate = None
    repeat = None
    toggle = None
    trigger = None


class MidiNote:
    """
    An object representing a MIDI Note
    """

    @property
    def duration(self) -> int:
        """
        Get the duration of the MIDI Note.
        """
        return 0

    @property
    def mute(self) -> bool:
        """
        Get/set the mute state of the MIDI Note.
        """
        return False

    @property
    def note_id(self) -> int:
        """
        Get the note id of the MIDI Note.
        """
        return 0

    @property
    def pitch(self) -> int:
        """
        Get the pitch of the MIDI Note.
        """
        return 0

    @property
    def probability(self) -> float:
        """
        Get/set the probability of the MIDI Note.
        """
        return 0.0

    @property
    def release_velocity(self) -> int:
        """
        Get/set the release velocity of the MIDI Note.
        """
        return 0

    @property
    def start_time(self) -> int:
        """
        Get/set the start time of the MIDI Note.
        """
        return 0

    @property
    def velocity(self) -> int:
        """
        Get/set the velocity of the MIDI Note.
        """
        return 0

    @property
    def velocity_deviation(self) -> int:
        """
        Get/set the velocity deviation of the MIDI Note.
        """
        return 0


class MidiNoteSpecification:
    """
    An object specifying the data for creating a MIDI note. To be used with the add_new_notes function.
    """


class MidiNoteVector(Vector):
    """
    A container for holding MIDI notes from Live.
    """

    def append(self, arg2: MidiNote):
        """
        Append a MIDI note to the vector.
        """
        return


class WarpMarker:
    """
    An object representing a Warp Marker
    """

    @property
    def beat_time(self) -> float:
        """
        Get the beat time of the Warp Marker.
        """
        return 0.0

    @property
    def sample_time(self) -> float:
        """
        Get the sample time of the Warp Marker.
        """
        return 0.0


class WarpMarkerVector(Vector):
    """
    A container for holding Warp Markers from Live.
    """

    def append(self, arg2: WarpMarker):
        """
        Append a Warp Marker to the vector.
        """
        return


class WarpMode:
    beatsValue = 0
    complexValue = 0
    complex_proValue = 0
    countValue = 0
    repitchValue = 0
    rexValue = 0
    textureValue = 0
    tonesValue = 0


class Clip:
    """
    This class represents a Clip in Live. It can be either an AudioClip or a MIDI Clip, in an Arrangement or the Session, dependingon the Track (Slot) it lives in.
    """

    class View:
        """
        Representing the view aspects of a Clip.
        """

        @property
        def _live_ptr(self) -> int:
            """
            Get the pointer to the Live Object.
            """
            return 0

        @property
        def canonical_parent(self):
            """
            Get the canonical parent of the Clip.View.
            """
            return None

        @property
        def grid_is_triplet(self) -> bool:
            """
            Get/set wether the grid is showing in triplet mode.
            """
            return False

        @property
        def grid_quantization(self):
            """
            Get/set clip grid quantization resolution.
            """
            return

        def hide_envelope(self):
            """
            Hide the envelope view.
            """
            return

        def select_envelope_parameter(self, arg2: DeviceParameter):
            """
            Select the given device parameter in the envelope view.
            """
            return DeviceParameter()

        def show_envelope(self):
            """
            Show the envelope view.
            """
            return

        def show_loop(self):
            """
            Show the entire loop in the detail view.
            """
            return

    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def available_warp_modes(self):
        """
        :return: Available for AudioClips only.Get/Set the available warp modes, that can be used.
        """
        return

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the Clip.
        """
        return None

    @property
    def color(self) -> int:
        """
        :return: Get/set the color of the Clip.
        """
        return 0

    @property
    def color_index(self) -> int:
        """
        :return: Get/set the color index of the Clip.
        """
        return 0

    @property
    def end_marker(self) -> float:
        """
        :return: Get/set the Clips end marker pos in beats/seconds (unit depends on warping).
        """
        return 0.0

    @property
    def end_time(self) -> float:
        """
        :return: Get/set the end time of the Clip.
        """
        return 0.0

    @property
    def file_path(self) -> str:
        """
        :return: Get the path of the file represented by the Audio Clip.
        """
        return ""

    @property
    def gain(self) -> float:
        """
        :return: Available for AudioClips only.Read/write access to the gain setting of theAudio Clip
        """
        return 0.0

    @property
    def gain_display_string(self) -> str:
        """
        :return: string with the gain as dB value
        """
        return ""

    @property
    def groove(self) -> Groove:
        """
        :return: Get/set the groove of the Clip.
        """
        return Groove()

    @property
    def has_envelopes(self) -> bool:
        """
        :return: Get/set the has envelopes state of the Clip.
        """
        return False

    @property
    def has_groove(self) -> bool:
        """
        :return: Get the has groove state of the Clip.
        """
        return False

    @property
    def is_arrangement_clip(self) -> bool:
        """
        :return: Get the is arrangement clip state of the Clip.
        """
        return False

    @property
    def is_audio_clip(self) -> bool:
        """
        :return: True if this Clip is an Audio Clip.A Clip can be either an Audio clip or a MIDI Clip.
        """
        return False

    @property
    def is_midi_clip(self) -> bool:
        """
        :return: True if this Clip is a MIDI Clip.A Clip can be either an Audio clip or a MIDI Clip.
        """
        return False

    @property
    def is_overdubbing(self) -> bool:
        """
        :return: Get/set the is overdubbing state of the Clip.
        """
        return False

    @property
    def is_playing(self) -> bool:
        """
        :return: Get/Set if this Clip is currently playing. If the Clips trigger mode is set to a quantization value, the Clip will not start playing immediately.
        If you need to know whether the Clip was triggered, use the is_triggered property.
        """
        return False

    @property
    def is_recording(self) -> bool:
        """
        :return: Get/set the is recording state of the Clip.
        """
        return False

    @property
    def is_triggered(self) -> bool:
        """
        :return: Get the is triggered state of the Clip.
        """
        return False

    @property
    def launch_mode(self) -> LaunchMode:
        """
        :return: Get/set the launch mode of the Clip.
        """
        return LaunchMode()

    @property
    def launch_quantization(self):
        """
        :return: Get/set the launch quantization of the Clip.
        """
        return

    @property
    def legato(self) -> bool:
        """
        :return: Get/set the legato state of the Clip.
        """
        return False

    @property
    def length(self) -> float:
        """
        :return: Get to the Clips length in beats/seconds (unit depends on warping).
        """
        return 0.0

    @property
    def loop_end(self) -> float:
        """
        :return: Get/set the loop end pos of this Clip in beats/seconds (unit depends on warping).
        """
        return 0.0

    @property
    def loop_start(self) -> float:
        """
        :return: Get/set the loop start pos in beats/seconds (unit depends on warping).
        """
        return 0.0

    @property
    def looping(self) -> bool:
        """
        :return: Get/Set the Clips 'loop is enabled' flag.
        Only Warped Audio Clips or MIDI Clip can be looped.
        """
        return False

    @property
    def muted(self) -> bool:
        """
        :return: Get/set the muted state of the Clip.
        """
        return False

    @property
    def name(self) -> str:
        """
        :return: Get/set the name of the Clip.
        """
        return ""

    @property
    def pitch_coarse(self) -> int:
        """
        Available for AudioClips only.
        :return: Read/write access to the pitch (in halftones) setting of theAudio Clip, ranging from -48 to 48.
        """
        return 0

    @property
    def pitch_fine(self) -> int:
        """
        Available for AudioClips only.
        :return: Read/write access to the pitch fine setting of theAudio Clip, ranging from -500 to 500.
        """
        return 0

    @property
    def playing_position(self) -> float:
        """
        :return: Get/set the playing position of the Clip.
        """
        return 0.0

    @property
    def playing_status(self) -> int:
        """
        :return: Get/set the playing status of the Clip.
        """
        return 0

    @property
    def position(self) -> float:
        """
        :return: Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).
        """
        return 0.0

    @property
    def ram_mode(self) -> int:
        """
        :return: Available for AudioClips only.Read/write access to the Ram mode setting of the Audio Clip.
        """
        return 0

    @property
    def sample_length(self) -> int:
        """
        Available for AudioClips only.
        :return: Get the sample length in sample time or -1 if there is no sample available.
        """
        return 0

    @property
    def signature_denominator(self) -> int:
        """
        :return: Get/set the signature denominator of the Clip.
        """
        return 0

    @property
    def signature_numerator(self) -> int:
        """
        :return: Get/set the signature numerator of the Clip.
        """
        return 0

    @property
    def start_marker(self) -> float:
        """
        :return: Get/set the Clips start marker pos in beats/seconds (unit depends on warping).
        """
        return 0.0

    @property
    def start_time(self) -> float:
        """
        :return: Get/set the start time of the Clip.
        """
        return 0.0

    @property
    def velocity_amount(self) -> float:
        """
        :return: Get/set the velocity amount of the Clip.
        """
        return 0.0

    @property
    def view(self) -> View:
        """
        :return: Get the Clip view.
        """
        return self.View()

    @property
    def warp_markers(self):
        """
        :return: Get/set the warp markers of the Clip.
        """
        return

    @property
    def warp_mode(self) -> int:
        """
        :return: Get/set the warp mode of the Clip.
        """
        return 0

    @property
    def warping(self) -> bool:
        """
        :return: Get/set the warping state of the Clip.
        """
        return False

    @property
    def will_record_on_start(self) -> bool:
        """
        :return: Get the will record on start state of the Clip.
        """
        return False

    def add_color_index_listener(self, arg2: Callable):
        """
        Add a listener to the color index of the Clip.
        """
        return

    def add_color_listener(self, arg2: Callable):
        """
        Add a listener to the color of the Clip.
        """
        return

    def add_end_marker_listener(self, arg2: Callable):
        """
        Add a listener to the end marker of the Clip.
        """
        return

    def add_end_time_listener(self, arg2: Callable):
        """
        Add a listener to the end time of the Clip.
        """
        return

    def add_file_path_listener(self, arg2: Callable):
        """
        Add a listener to the file path of the Clip.
        """
        return

    def add_gain_listener(self, arg2: Callable):
        """
        Add a listener to the gain of the Clip.
        """
        return

    def add_groove_listener(self, arg2: Callable):
        """
        Add a listener to the groove of the Clip.
        """
        return

    def add_has_envelopes_listener(self, arg2: Callable):
        """
        Add a listener to the has envelopes of the Clip.
        """
        return

    def add_is_overdubbing_listener(self, arg2: Callable):
        """
        Add a listener to the is overdubbing of the Clip.
        """
        return

    def add_is_recording_listener(self, arg2: Callable):
        """
        Add a listener to the is recording of the Clip.
        """
        return

    def add_launch_mode_listener(self, arg2: Callable):
        """
        Add a listener to the launch mode of the Clip.
        """
        return

    def add_launch_quantization_listener(self, arg2: Callable):
        """
        Add a listener to the launch quantization of the Clip.
        """
        return

    def add_legato_listener(self, arg2: Callable):
        """
        Add a listener to the legato of the Clip.
        """
        return

    def add_loop_end_listener(self, arg2: Callable):
        """
        Add a listener to the loop end of the Clip.
        """
        return

    def add_loop_jump_listener(self, arg2: Callable):
        """
        Add a listener to the loop jump of the Clip.
        """
        return

    def add_loop_start_listener(self, arg2: Callable):
        """
        Add a listener to the loop start of the Clip.
        """
        return

    def add_looping_listener(self, arg2: Callable):
        """
        Add a listener to the looping of the Clip.
        """
        return

    def add_muted_listener(self, arg2: Callable):
        """
        Add a listener to the muted of the Clip.
        """
        return

    def add_name_listener(self, arg2: Callable):
        """
        Add a listener to the name of the Clip.
        """
        return

    def add_notes_listener(self, arg2: Callable):
        """
        Add a listener to the notes of the Clip.
        """
        return

    def add_pitch_coarse_listener(self, arg2: Callable):
        """
        Add a listener to the pitch coarse of the Clip.
        """
        return

    def add_pitch_fine_listener(self, arg2: Callable):
        """
        Add a listener to the pitch fine of the Clip.
        """
        return

    def add_playing_position_listener(self, arg2: Callable):
        """
        Add a listener to the playing position of the Clip.
        """
        return

    def add_playing_status_listener(self, arg2: Callable):
        """
        Add a listener to the playing status of the Clip.
        """
        return

    def add_position_listener(self, arg2: Callable):
        """
        Add a listener to the position of the Clip.
        """
        return

    def add_ram_mode_listener(self, arg2: Callable):
        """
        Add a listener to the ram mode of the Clip.
        """
        return

    def add_signature_denominator_listener(self, arg2: Callable):
        """
        Add a listener to the signature denominator of the Clip.
        """
        return

    def add_signature_numerator_listener(self, arg2: Callable):
        """
        Add a listener to the signature numerator of the Clip.
        """
        return

    def add_start_marker_listener(self, arg2: Callable):
        """
        Add a listener to the start marker of the Clip.
        """
        return

    def add_velocity_amount_listener(self, arg2: Callable):
        """
        Add a listener to the velocity amount of the Clip.
        """
        return

    def add_warp_markers_listener(self, arg2: Callable):
        """
        Add a listener to the warp markers of the Clip.
        """
        return

    def add_warp_mode_listener(self, arg2: Callable):
        """
        Add a listener to the warp mode of the Clip.
        """
        return

    def add_warping_listener(self, arg2: Callable):
        """
        Add a listener to the warping of the Clip.
        """
        return

    def apply_note_modifications(self, arg2: MidiNoteVector):
        """
        Expects a list of notes as returned from get_notes_extended.
        The content of the list will be used to modify existing notes in the clip, based on matching note IDs.
        This function should be used when modifying existing notes, e.g. changing the velocity or start time.
        The function ensures that per-note events attached to the modified notes are preserved.
        This is NOT the case when replacing notes via a combination of remove_notes_extended and add_new_notes.
        The given list can be a subset of the notes in the clip, but it must not contain any notes that are not present in the clip.
        """
        return

    def automation_envelope(self, arg2: DeviceParameter) -> AutomationEnvelope:
        """
        :return: Return the envelope for the given parameter. Returns None if the envelope doesn't exist or for Arrangement clips or for parameters from a different track.
        """
        return AutomationEnvelope()

    def beat_to_sample_time(self, beat_time: float) -> float:
        """
        Available for AudioClips only.
        :return: Converts the given beat time to sample time.
        """
        return 0.0

    def clear_all_envelopes(self):
        """
        Remove all envelopes from the Clip.
        """
        return

    def clear_envelope(self, arg2: DeviceParameter):
        """
        Remove the envelope for the given parameter.
        """
        return

    def color_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "color".
        """
        return False

    def color_index_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "color_index".
        """
        return False

    def create_automation_envelope(self, arg2: DeviceParameter) -> AutomationEnvelope:
        """
        Creates an envelope for a given parameter and returns it.
        This should only be used if the envelope doesn't exist.
        Raises an error if the envelope can't be created.
        """
        return AutomationEnvelope()

    def crop(self):
        """
        The region that is cropped depends on whether the clip is looped or not.
        If looped, the region outside the loop is removed.
        If not looped, the region outside the start and end markers is removed.
        """
        return

    def deselect_all_notes(self):
        """
        Deselect all notes in the clip.
        """
        return

    def duplicate_loop(self):
        """
        Make the loop two times longer and duplicates notes and envelopes.
        Duplicates the clip start/end range if the clip is not looped.
        """
        return

    def duplicate_region(self, region_start: float, region_length: float, destination_time: float, pitch: int = -1, transposition_amount: int = 0):
        """
        Duplicate the notes in the specified region to the destination_time.
        Only notes of the specified pitch are duplicated or all if pitch is -1.
        If the transposition_amount is not 0, the notes in the region will be transposed by the transpose_amount of semitones.
        Raises an error on audio clips.
        """
        return

    def end_marker_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "end_marker".
        """
        return False

    def end_time_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "end_time".
        """
        return False

    def file_path_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "file_path".
        """
        return False

    def fire(self):
        """
        (Re)Fire the Clip.
        """
        return

    def gain_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "gain".
        """
        return False

    def get_notes(self, from_time: float, from_pitch: int, time_span: float, pitch_span: int) -> MidiNoteVector:
        """
        Returns a tuple of tuples where each inner tuple represents a note starting in the given pitch- and time range.
        The inner tuple contains pitch, time, duration, velocity, and mute state.
        """
        return MidiNoteVector()

    def get_notes_by_id(self, arg2) -> MidiNoteVector:
        """
        Return a list of MIDI notes matching the given note IDs.
        """
        return MidiNoteVector()

    def get_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> MidiNoteVector:
        """
        Returns a tuple of tuples where each inner tuple represents a note starting in the given pitch- and time range.
        The inner tuple contains pitch, time, duration, velocity, mute state, and note ID.
        """
        return MidiNoteVector()

    def get_selected_notes(self) -> MidiNoteVector:
        """
        Returns a tuple of tuples where each inner tuple represents a selected note.
        The inner tuple contains pitch, time, duration, velocity, and mute state.
        """
        return MidiNoteVector()

    def get_selected_notes_extended(self) -> MidiNoteVector:
        """
        Returns a list of all MIDI notes from the clip that are currently selected. Each note is represented by a Live.Clip.MidiNote object.
        The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
        """
        return MidiNoteVector()

    def groove_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "groove".
        """
        return False

    def has_envelopes_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "has_envelopes".
        """
        return False

    def is_recording_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "is_recording".
        """
        return False

    def launch_mode_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "launch_mode".
        """
        return False

    def launch_quantization_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "launch_quantization".
        """
        return False

    def legato_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "legato".
        """
        return False

    def loop_end_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "loop_end".
        """
        return False

    def loop_jump_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "loop_jump".
        """
        return False

    def loop_start_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "loop_start".
        """
        return False

    def looping_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "looping".
        """
        return False

    def move_playing_pos(self, time: float):
        """
        Move the playing position of the Clip.
        """
        return

    def muted_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "muted".
        """
        return False

    def name_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "name".
        """
        return False

    def pitch_coarse_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "pitch_coarse".
        """
        return False

    def pitch_fine_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "pitch_fine".
        """
        return False

    def playing_position_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "playing_position".
        """
        return False

    def playing_status_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "playing_status".
        """
        return False

    def position_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "position".
        """
        return False

    def ram_mode_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "ram_mode".
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

    def remove_end_marker_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "end_marker".
        """
        return

    def remove_end_time_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "end_time".
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

    def remove_groove_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "groove".
        """
        return

    def remove_has_envelopes_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_envelopes".
        """
        return

    def remove_is_overdubbing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_overdubbing".
        """
        return

    def remove_is_recording_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_recording".
        """
        return

    def remove_launch_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "launch_mode".
        """
        return

    def remove_launch_quantization_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "launch_quantization".
        """
        return

    def remove_legato_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "legato".
        """
        return

    def remove_loop_end_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "loop_end".
        """
        return

    def remove_loop_jump_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "loop_jump".
        """
        return

    def remove_loop_start_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "loop_start".
        """
        return

    def remove_looping_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "looping".
        """
        return

    def remove_muted_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "muted".
        """
        return

    def remove_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        return

    def remove_notes(self, arg2: float, arg3: int, arg4: float, arg5: int):
        """
        Delete all notes starting in the given pitch and time range.
        """
        return

    def remove_notes_extended(self, from_pitch: int, pitch_spawn: int, from_time: float, time_span: float):
        """
        Delete all notes starting in the given pitch and time range.
        This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events.
        apply_note_modifications must be used instead for modifying existing notes.
        """
        return

    def remove_notes_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "notes".
        """
        return

    def remove_pitch_coarse_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "pitch_coarse".
        """
        return

    def remove_pitch_fine_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "pitch_fine".
        """
        return

    def remove_playing_position_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playing_position".
        """
        return

    def remove_playing_status_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playing_status".
        """
        return

    def remove_position_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "position".
        """
        return

    def remove_ram_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ram_mode".
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

    def remove_start_marker_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "start_marker".
        """
        return

    def remove_velocity_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "velocity_amount".
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

    def sample_to_beat_time(self, sample_time: float) -> float:
        """
        Available for AudioClips only.
        :return: Converts the given sample time to beat time.
        """
        return 0.0

    def scrub(self, scrub_position: float):
        """
        Scrubs inside a clip.
        scrub_position defines the position in beats that the scrub will start from.
        The scrub will continue until stop_scrub is called. Global quantization applies to the scrub's position and length.
        """
        return

    def seconds_to_sample_time(self, seconds: float) -> float:
        """
        Available for AudioClips only.
        :return: Converts the given seconds to sample time. Raises an error if the sample is warped.
        """
        return 0.0

    def select_all_notes(self):
        """
        Selects all notes present in the clip.
        """
        return

    def set_fire_button_state(self, state: bool):
        """
        Set the clip's fire button state directly. Supports all launch modes.
        """
        return

    def set_notes(self, notes: tuple):
        """
        Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_notes.
        The notes described that way will then be added to the clip.
        """
        return

    def signature_denominator_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "signature_denominator".
        """
        return False

    def signature_numerator_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "signature_numerator".
        """
        return False

    def start_marker_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "start_marker".
        """
        return False

    def stop(self):
        """
        Stop playing this Clip.
        """
        return

    def stop_scrub(self):
        """
        Stops the current scrub.
        """
        return

    def velocity_amount_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "velocity_amount".
        """
        return False

    def warp_markers_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "warp_markers".
        """
        return False

    def warp_mode_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "warp_mode".
        """
        return False

    def warping_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "warping".
        """
        return False

