# All referenced (missing descriptions)
from typing import Optional, Callable, Any
from Live.Base import Vector
from Live.Browser import Browser
from Live.Song import Song
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
    :return: Returns the application object
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
    def unavailable_features(self) -> 'UnavailableFeatureVector':
        """
        :return: List of unavailable features due to current edition of Ableton Live.
        """
        return UnavailableFeatureVector()

    @property
    def view(self) -> 'Application.View':
        """
        :return: The current view.
        """
        return Application.View()

    def add_control_surface_listener(self, arg2: Callable) -> None:
        """
        :param arg2: The listener that will be called when a control surface is added or removed.
        """

    def add_open_open_dialog_count_listener(self, arg2: Callable) -> None:
        """
        :param arg2: The listener that will be called when the open dialog count changes.
        """

    def add_unavailable_features_listener(self, arg2: Callable) -> None:
        """
        :param arg2: The listener that will be called when the unavailable features change.
        """

    def control_surfaces_has_listener(self, arg2: Callable) -> bool:
        """
        :param arg2: The function or method to check for.
        :return: True if the listener is connected to the property "control_surfaces", False otherwise.
        """

    def get_bugfix_version(self) -> int:
        """
        :return: The bugfix version of Ableton Live.
        """

    def get_document(self) -> 'Song':
        """
        :return: The current Live Set.
        """

    def get_major_version(self) -> int:
        """
        :return: The major version of Ableton Live.
        """

    def get_minor_version(self) -> int:
        """
        :return: The minor version of Ableton Live.
        """

    def has_option(self, arg2: Any) -> bool:
        """
        :param arg2: The option to check for.
        :return: True if the option exists in Options.txt, False otherwise.
        """

    def open_dialog_count_has_listener(self, arg2: Callable) -> bool:
        """
        :param arg2: The function or method to check for.
        :return: True if the listener is connected to the property "open_dialog_count", False otherwise.
        """

    def press_current_dialog_button(self, arg2: int) -> None:
        """
        Press a button with its index in the current message box.

        :param arg2: The index of the button to press.
        """

    def remove_control_surface_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener from property "control_surfaces".

        :param arg2: The listener to remove.
        """

    def remove_open_dialog_count_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener from property "open_dialog_count".

        :param arg2: The listener to remove.
        """

    def remove_unavailable_features_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener from property "unavailable_features".

        :param arg2: The listener to remove.
        """

    def unavailable_features_has_listener(self, arg2: Callable) -> bool:
        """
        :param arg2: The function or method to check for.
        :return: True if the listener is connected to the property "unavailable_features", False otherwise.
        """

    class View:
        @property
        def _live_ptr(self) -> int:
            """
            :return: The pointer to the Live object.
            """
            return 0

        @property
        def browse_mode(self) -> bool:
            """
            :return: True if HotSwap mode is active for any target.
            """
            return False

        @property
        def canonical_parent(self) -> Optional['Application.View']:
            """
            :return: The canonical parent of the application view.
            """
            return Application.View()

        @property
        def focused_document_view(self) -> str:
            """
            :return: The name of the document view ('Session' or 'Arranger') shown in the currently selected window.
            """
            return ''

        def add_browse_mode_listener(self, arg2: Callable) -> None:
            """
            :param arg2: The listener that will be called when the property "browse_mode" has changed.
            """

        def add_focused_document_view_listener(self, arg2: Callable) -> None:
            """
            :param arg2: The listener that will be called when the property "focused_document_view" has changed.
            """

        def add_is_view_visible_listener(self, arg2: Callable, arg3: str) -> None:
            """
            :param arg2: The listener that will be called when the property "is_view_visible" has changed.
            :param arg3: The identifier string.
            """

        def add_view_focus_changed_listener(self, arg2: Callable) -> None:
            """
            :param arg2: The listener that will be called when the property "view_focus_changed" has changed.
            """

        def available_main_views(self) -> list[str]:
            """
            :return: A list of strings with the available subcomponent views.
            """

        def browse_mode_has_listener(self, arg2: Callable) -> bool:
            """
            :param arg2: The function or method to check for.
            :return: True if the listener is connected to the property "browse_mode", False otherwise.
            """

        def focus_view(self, arg2: str) -> None:
            """
            :param arg2: The identifier string of the view to focus.
            """

        def focused_document_view_has_listener(self, arg2: Callable) -> bool:
            """
            :param arg2: The function or method to check for.
            :return: True if the listener is connected to the property "focused_document_view", False otherwise.
            """

        def hide_view(self, arg2: str) -> None:
            """
            :param arg2: The identifier string of the view to hide.
            """

        def is_view_visible(self, arg2: str, arg3: bool = True) -> bool:
            """
            :param arg2: The identifier string of the view to check.
            :param arg3: True if main window only, False otherwise.
            :return: True if the view is visible, False otherwise.
            """

        def is_view_visible_has_listener(self, arg2: str, arg3: Callable) -> bool:
            """
            :param arg2: The identifier string of the view.
            :param arg3: The function or method to check for.
            :return: True if the listener is connected to the property "is_view_visible", False otherwise.
            """

        def remove_browse_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener from property "browse_mode".

            :param arg2: The listener to remove.
            """

        def remove_focused_document_view_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener from property "focused_document_view".

            :param arg2: The listener to remove.
            """

        def remove_is_view_visible_listener(self, arg2: str, arg3: Callable) -> None:
            """
            :param arg2: The identifier string of the view.
            :param arg3: The listener to remove.
            """

        def remove_view_focus_changed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener from property "view_focus_changed".

            :param arg2: The listener to remove.
            """

        def scroll_view(self, arg2: int, arg3: str, arg4: bool) -> None:
            """
            :param arg2: The direction to scroll.
            :param arg3: The identifier string of the view to scroll.
            :param arg4: True if possible, False otherwise.
            """

        def show_view(self, arg2: str) -> None:
            """
            :param arg2: The identifier string of the view to show.
            """

        def toggle_browse(self) -> None:
            """
            :return: Reveals the device chain, the browser and starts hot swap for the selected device.
            """

        def view_focus_changed_has_listener(self, arg2: Callable) -> bool:
            """
            :param arg2: The function or method to check for.
            :return: True if the listener is connected to the property "view_focus_changed", False otherwise.
            """

        def zoom_view(self, arg2: int, arg3: str, arg4: bool) -> None:
            """
            :param arg2: The direction to zoom.
            :param arg3: The identifier string of the view to zoom.
            :param arg4: True if possible, False otherwise.
            """

        class NavDirection:
            down = None
            left = None
            right = None
            up = None


class UnavailableFeature:
    note_velocity_ranges_and_probabilities = None


class UnavailableFeatureVector(Vector):
    def append(self, arg2: UnavailableFeature) -> None:
        pass

    def extend(self, arg2: UnavailableFeature) -> None:
        pass
