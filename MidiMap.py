# All referenced (missing descriptions)
from Live.DeviceParameter import DeviceParameter


class CCFeedbackRule:
    """
    Structure to define feedback properties of MIDI mappings.
    """
    @property
    def cc_no(self):
        """
        ???
        """
        return

    @property
    def cc_value_map(self):
        """
        ???
        """
        return

    @property
    def channel(self):
        """
        ???
        """
        return

    @property
    def delay_in_ms(self):
        """
        ???
        """
        return


class MapMode:
    absolute = None
    absolute_14_bit = None
    relative_binary_offset = None
    relative_signed_bit = None
    relative_signed_bit2 = None
    relative_smooth_binary_offset = None
    relative_smooth_signed_bit = None
    relative_smooth_signed_bit2 = None
    relative_smooth_two_compliment = None
    relative_two_compliment = None


class NoteFeedbackRule:
    """
    Structure to define feedback properties of MIDI mappings.
    """
    @property
    def channel(self):
        """
        ???
        """
        return

    @property
    def delay_in_ms(self):
        """
        ???
        """
        return

    @property
    def note_no(self):
        """
        ???
        """
        return

    @property
    def vel_map(self):
        """
        ???
        """
        return


class PitchBendFeedbackRule:
    """
    Structure to define feedback properties of MIDI mappings.
    """
    @property
    def channel(self):
        """
        ???
        """
        return

    @property
    def delay_in_ms(self):
        """
        ???
        """
        return

    @property
    def value_pair_map(self):
        """
        ???
        """
        return


def forward_midi_cc(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool = True) -> bool:
    """
    ???
    """
    return False


def forward_midi_note_on(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool = True) -> bool:
    """
    ???
    """
    return False


def forward_midi_pitchbend(arg1: int, arg2: int, arg3: int) -> bool:
    """
    ???
    """
    return False


def map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float = 1.0) -> bool:
    """
    ???
    """
    return False


def map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float = 1.0) -> bool:
    """
    ???
    """
    return False


def map_midi_note(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int) -> bool:
    """
    ???
    """
    return False


def map_midi_note_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int, arg5: NoteFeedbackRule) -> bool:
    """
    ???
    """
    return False


def map_midi_pitchbend(arg1: int, arg2: DeviceParameter, arg3: int, arg4: bool) -> bool:
    """
    ???
    """
    return False


def map_midi_pitchbend_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: PitchBendFeedbackRule, arg5: bool) -> bool:
    """
    ???
    """
    return False


def send_feedback_for_parameter(arg1: int, arg2: DeviceParameter):
    """
    ???
    """
    return
