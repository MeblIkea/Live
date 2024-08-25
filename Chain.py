# All referenced (missing descriptions)
from typing import Callable
from Live.Base import Vector
from Live.ChainMixerDevice import ChainMixerDevice
from Live.Device import Device


class Chain:
    """
    This class represents a group device chain in Live
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
        Get the canonical parent of the chain.
        """
        return

    @property
    def color(self) -> int:
        """
        Access the color index of the Chain.
        """
        return 0

    @property
    def color_index(self) -> int:
        """
        Access the color index of the Chain.
        """
        return 0

    @property
    def devices(self) -> Vector[Device]:
        """
        Return const access to all available Devices that are present in the chains
        """
        return Vector()

    @property
    def has_audio_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is true for all Audio Chains.
        """
        return False

    @property
    def has_audio_output(self) -> bool:
        """
        return True, if this Chain sends out an Audio signal. This is true for all Audio Chains, and MIDI chains with an Instrument.
        """
        return False

    @property
    def has_midi_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is true for all MIDI Chains.
        """
        return False

    @property
    def has_midi_output(self) -> bool:
        """
        return True, if this Chain sends out MIDI events. This is true for all MIDI Chains with no Instruments.
        """
        return False

    @property
    def is_auto_colored(self) -> bool:
        """
        Get/set access to the auto color flag of the Chain.
        If True, the Chain will always have the same color as the containing Track or Chain.
        """
        return False

    @property
    def mixer_device(self) -> ChainMixerDevice:
        """
        Return access to the mixer device that holds the chain's mixer parameters:
        the Volume, Pan, and Send amounts.
        """
        return ChainMixerDevice()

    @property
    def mute(self) -> bool:
        """
        Mute/unmute the chain.
        """
        return False

    @property
    def muted_via_solo(self) -> bool:
        """
        Return const access to whether this chain is muted due to some other chain being soloed.
        """
        return False

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the Chain, as visible in the track header.
        """
        return ""

    @property
    def solo(self) -> bool:
        """
        Get/Set the solo status of the chain. Note that this will not disable the solo state of any other Chain in the same rack.
        If you want exclusive solo, you have to disable the solo state of the other Chains manually.
        """
        return False

    def add_color_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        pass

    def add_color_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        pass

    def add_devices_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "devices" has changed.
        """
        pass

    def add_is_auto_colored_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "is_auto_colored" has changed.
        """
        pass

    def add_mute_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mute" has changed.
        """
        pass

    def add_muted_via_solo_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
        """
        pass

    def add_name_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        pass

    def add_solo_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "solo" has changed.
        """
        pass

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

    def delete_device(self, arg2: int):
        """
        Remove a device identified by its index from the chain. Throws runtime error if bad index.
        """
        pass

    def devices_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "devices".
        """
        return False

    def is_auto_colored_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_auto_colored".
        """
        return False

    def mute_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mute".
        """
        return False

    def muted_via_solo_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "muted_via_solo".
        """
        return False

    def name_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        return False

    def remove_color_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "color_index".
        """
        pass

    def remove_color_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "color".
        """
        pass

    def remove_devices_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "devices".
        """
        pass

    def remove_is_auto_colored_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_auto_colored".
        """
        pass

    def remove_mute_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mute".
        """
        pass

    def remove_muted_via_solo_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "muted_via_solo".
        """
        pass

    def remove_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        pass

    def remove_solo_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "solo".
        """
        pass

    def solo_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "solo".
        """
        return False
