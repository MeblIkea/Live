# All referenced
from typing import Callable
from Live.Groove import Groove


class GroovePool:
    """
    This class represents the groove pool in Live.
    """
    @property
    def _live_ptr(self) -> int:
        """
        Pointer to the Live Object
        """
        return 0

    @property
    def grooves(self) -> list[Groove]:
        """
        List of Grooves
        """
        return []

    def add_grooves_listener(self, arg2: Callable):
        """
        Add a listener to when the property "grooves" changes.
        """
        return

    def grooves_has_listener(self, arg2: Callable) -> bool:
        """
        Check if a listener is registered to the property "grooves"
        """
        return False

    def remove_grooves_listener(self, arg2: Callable):
        """
        Remove a listener from the property "grooves"
        """
        return
