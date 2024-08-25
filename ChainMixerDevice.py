# All referenced (missing descriptions)
from typing import Callable


class ChainMixerDevice:
    """
    This class represents a Chain's Mixer Device in Live, which gives you access to the Volume, Panning, and Send properties of a Chain.
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
        Get the canonical parent of the mixer device.
        """
        return

    @property
    def chain_activator(self):
        """
        Const access to the Chain's Activator Device Parameter.
        """
        return

    @property
    def panning(self):
        """
        Const access to the Chain's Panning Device Parameter.
        """
        return

    @property
    def sends(self):
        """
        Const access to the Chain's list of Send Amount Device Parameters.
        """
        return

    @property
    def volume(self):
        """
        Const access to the Chain's Volume Device Parameter.
        """
        return

    def add_sends_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "sends" has changed.
        """
        pass

    def remove_sends_listener(self, arg2: Callable):
        """
        Remove a listener function or method, which was previously added to the property "sends".
        """
        pass

    def sends_has_listener(self, arg2: Callable) -> bool:
        """
        Check if a listener function or method is already registered to the property "sends".
        """
        return False
