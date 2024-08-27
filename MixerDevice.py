# All referenced (missing descriptions)
from typing import Callable


class MixerDevice:
    """
    Mixer Device in Live, which gives you access to the Volume and Panning properties of a Track.
    """
    class crossfade_assignments:
        A = None
        B = None
        NONE = None

    class panning_modes:
        setero = None
        stereo_split = None

    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the Device.View.
        """
        return None

    @property
    def crossfade_assign(self) -> 'MixerDevice.crossfade_assignments':
        """
        Player and ReturnTracks only.
        :return: Access to the Track's Crossfade Assign State.
        """
        return MixerDevice.crossfade_assignments()

    @property
    def crossfader(self):
        """
        MasterTrack only.
        :return: Const access to the Crossfader.
        """
        return

    @property
    def cue_volume(self):
        """
        MasterTrack only.
        :return: Const access to the Cue Volume Parameter.
        """
        return

    @property
    def left_split_stereo(self):
        """
        :return: Const access to the Track's Left Split Stereo Panning Device Parameter.
        """
        return

    @property
    def panning(self):
        """
        :return: Const access to the Tracks Panning Device Parameter.
        """
        return

    @property
    def panning_mode(self) -> 'MixerDevice.panning_modes':
        """
        :return: Access to the Track's Panning Mode.
        """
        return MixerDevice.panning_modes()

    @property
    def right_split_stereo(self):
        """
        :return: Const access to the Track's Right Split Stereo Panning Device Parameter.
        """
        return

    @property
    def sends(self):
        """
        :return: Const access to the Tracks list of Send Amount Device Parameters.
        """
        return

    @property
    def song_tempo(self):
        """
        MasterTrack only.
        :return: Const access to the Song's Tempo.
        """
        return

    @property
    def track_activator(self):
        """
        :return: Const access to the Track Activator Device Parameter.
        """
        return

    @property
    def volume(self):
        """
        :return: Const access to the Track Volume Device Parameter.
        """
        return

    def add_crossfade_assign_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "crossfade_assign" has changed.
        :param arg2: Listener function or method.
        """
        pass

    def add_panning_mode_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "panning_mode" has changed.
        :param arg2: Listener function or method.
        """
        pass

    def add_sends_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "sends" has changed.
        :param arg2: Listener function or method.
        """
        pass

    def crossfade_assign_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "crossfade_assign".
        :param arg2: Listener function or method.
        :return: True if listener is connected.
        """
        return False

    def panning_mode_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "panning_mode".
        :param arg2: Listener function or method.
        :return: True if listener is connected.
        """
        return False

    def remove_crossfade_assign_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "crossfade_assign".
        :param arg2: Listener function or method.
        """
        pass

    def remove_panning_mode_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "panning_mode".
        :param arg2: Listener function or method.
        """
        pass

    def remove_sends_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "sends".
        :param arg2: Listener function or method.
        """
        pass

    def sends_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "sends".
        :param arg2: Listener function or method.
        :return: True, if listener is connected.
        """
        return False
