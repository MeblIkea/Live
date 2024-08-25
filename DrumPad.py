# All referenced (missing descriptions)
from typing import Callable


class DrumPad:
    """
    This class represents a drum group device pad in Live.
    """
    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the Device.
        """
        return None

    @property
    def chains(self):
        """
        :return: Return const access to the list of chains in this drum pad.
        """
        return

    @property
    def mute(self) -> bool:
        """
        :return: Mute/unmute the pad.
        """
        return False

    @property
    def name(self) -> str:
        """
        :return: Access to the name of the device.
        """
        return ""

    @property
    def note(self):
        """
        :return: Get the MIDI note of the drum pad.
        """
        return

    @property
    def solo(self) -> bool:
        """
        :return: Solo/unsolo the pad.
        """
        return False

    def add_chains_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "chains" has changed.
        """
        pass

    def add_mute_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mute" has changed.
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

    def chains_has_listener(self, arg2: Callable) -> bool:
        """
        :returns: The given listener function or method is connected to the property "chains".
        """
        return False

    def delete_all_chains(self):
        """
        Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.
        """
        return

    def mute_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "mute".
        """
        return False

    def name_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "name".
        """
        return False

    def remove_chains_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "chains".
        """
        pass

    def remove_mute_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mute".
        """
        pass

    def remove_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        pass

    def remove_solo_listener(self, arg2: int, arg3: int):
        """
        Remove a previously set listener function or method from property "solo".
        """
        pass

    def solo_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "solo".
        """
        return False

