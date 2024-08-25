# All referenced (missing descriptions)
from typing import Callable
from Live.Chain import Chain


class DrumChain(Chain):
    """
    This class represents a drum group device chain in Live.
    """

    @property
    def choke_group(self):
        """
        Access to the chain's choke group setting.
        """
        return

    @property
    def out_note(self):
        """
        Access to the MIDI note sent to the devices in the chain.
        """
        return

    def add_choke_group_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "choke_group" has changed.
        """
        return

    def add_out_note_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "out_note" has changed.
        """
        return

    def choke_group_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "choke_group".
        """
        return False

    def out_note_has_listener(self, arg2: Callable) -> bool:
        """
        :return: if the given listener function or method is connected to the property "out_note".
        """
        return False

    def remove_choke_group_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "choke_group".
        """
        return

    def remove_out_note_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "out_note".
        """
        return
