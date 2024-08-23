from typing import List, Optional

from Live.Browser import Browser
from ableton.v3.control_surface import ControlSurface


def combine_apcs() -> bool:
    """
    :return: True if the two APCs are combined, False otherwise
    """


def encrypt_challenges(dongle1: int, dongle2: int, key_index: int = 0) -> tuple:
    """
    :param dongle1: The first dongle
    :param dongle2: The second dongle
    :param key_index: The key index
    :return: The encrypted challenges based on the TEA algorithm
    """


def encrypt_challenges2(arg1: int) -> int:
    """
    :param arg1: The challenge
    :return: UMAC hash for the given challenge
    """


def get_application() -> 'Application':
    """
    :return: The application
    """


def get_random_int(arg1: int, arg2: int) -> int:
    """
    :param arg1: Start of the range
    :param arg2: End of the range

    :return: A random integer
    """


class Application:
    @property
    def _live_ptr(self) -> int:
        """
        :return: The pointer to the Live object.
        """
        return 0

    @property
    def browser(self) -> Browser:
        """
        :return: An interface to the browser.
        """
        return Browser()

    @property
    def canonical_parent(self) -> Optional['Application']:
        """
        :return: The canonical parent.
        """
        return Application()

    @property
    def control_surfaces(self) -> list[Optional[ControlSurface]]:
        """
        :return: List of control surfaces in preferences in the right order. None if no control surfaces active at that index.
        """
        return []

    @property
    def current_dialog_button_count(self) -> int:
        """
        :return: The number of buttons in the current dialog.
        """
        return 0

    @property
    def open_dialog_count(self) -> int:
        """
        :return: The number of open dialogs (0 for none).
        """
        return 0

    @property
    def unavailable_features(self) -> List[str]:
        """
        :return: List of unavailable features due to current edition of Ableton Live.
        """
        return []
