# All referenced (missing descriptions)
from Clip import Clip
from Live.DrumPad import DrumPad
from Live.SimplerDevice import SimplerDevice
from Live.Song import Song


def audio_to_midi_clip(song: Song, audio_clip: Clip, audio_to_midi_type: int):
    """
    Creates a MIDI clip in a new MIDI track with the notes extracted from the given audio_clip.
    The `audio_to_midi_type` decides which algorithm is used in the process.
    Raises error when called with an inconvertible clip or invalid `audio_to_midi_type`.
    """
    return


def create_drum_rack_from_audio_clip(song: Song, audio_clip: Clip):
    """
    Creates a new track with a drum rack with a simpler on the first pad with the specified audio clip.
    """
    return


def create_midi_track_from_drum_pad(song: Song, drum_pad: DrumPad):
    """
    Creates a new Midi track containing the specified Drum Pad's device chain.
    """
    return


def create_midi_track_with_simpler(song: Song, audio_clip: Clip):
    """
    Creates a new Midi track with a simpler including the specified audio clip.
    """
    return


def is_convertible_to_midi(song: Song, audio_clip: Clip) -> bool:
    """
    Returns whether `audio_clip` can be converted to MIDI.
    Raises error when called with a MIDI clip
    """
    return False


def move_devices_on_track_to_new_drum_rack_pad(song: Song, track_index: int):
    """
    Moves the entire device chain of the track according to the track index onto the C1 (note 36) drum pad of a new drum rack in a new track.
    If the track associated with the track index does not contain any devices nothing changes (i.e. a new track and new drum rack are not created).
    """
    return


def sliced_simpler_to_drum_rack(song: Song, simpler: SimplerDevice):
    """
    Converts the Simpler into a Drum Rack, assigning each slice to a drum pad.
    Calling it on a non-sliced simpler raises an error.
    """
    return


class AudioToMidiType:
    drums_to_midi = None
    harmony_to_midi = None
    melody_to_midi = None
