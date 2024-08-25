# All referenced
class LomObject:
    """
    Base class for an object that is accessible via the LOM
    """
    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0
