from Live.Base import Vector
from Live.DeviceParameter import DeviceParameter


class AutomationEnvelope:
    def insert_step(self, arg2: float, arg3: float, arg4: float):
        return

    def value_at_time(self, arg2: float):
        return 0.0


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
