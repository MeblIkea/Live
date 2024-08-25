# All referenced (missing descriptions)
from typing import Callable


class Scene:
    """
    This class represents a series of ClipSlots in Lives Session view matrix.
    """
    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0

    @property
    def canonical_parent(self):
        """
        Get the canonical parent of the scene.
        """
        return

    @property
    def clip_slots(self):
        """
        return a list of clip slots (see class AClipSlot) that this scene covers.
        """
        return

    @property
    def color(self):
        """
        Get/set access to the color of the Scene (RGB).
        """
        return

    @property
    def color_index(self):
        """
        Get/set access to the color index of the Scene. Can be None for no color.
        """
        return

    @property
    def is_empty(self) -> bool:
        """
        Returns True if all clip slots of this scene are empty.
        """
        return False

    @property
    def is_triggered(self) -> bool:
        """
        Const access to the scene's trigger state.
        """
        return False

    @property
    def name(self) -> str:
        """
        Get/Set the name of the scene. Might contain the substring BPM, which identifies that the scene will change the tempo when fired.
        To Get/Set the temp, use the 'tempo' property of the scene.
        """
        return ""

    @property
    def tempo(self) -> float:
        """
        Get/Set the tempo value of the scene.
        The Song will use the Scenes tempo as soon as the Scene is fired.
        Returns -1 if the Scene has no tempo property.
        """
        return 0.0

    def add_clip_slots_listener(self, arg2: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "clip_slots" has changed.
        """
        return

    def add_color_index_listener(self, arg2: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        return

    def add_color_listener(self, arg2: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        return

    def add_is_triggered_listener(self, arg2: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_triggered" has changed.
        """
        return

    def add_name_listener(self, arg2: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        return

    def clip_slots_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "clip_slots".
        """
        return False

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

    def fire(self, force_legato: bool = False, can_select_scene_on_launch: bool = True) -> None:
        """
        Fire the scene directly. Will fire all clip slots that this scene owns and select the scene itself.
        """
        return

    def fire_as_selected(self, force_legato: bool = False) -> None:
        """
        Fire the selected scene. Will fire all clip slots that this scene owns and select the next scene if necessary.
        """
        return

    def is_triggered_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_triggered".
        """
        return False

    def name_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        return False

    def remove_clip_slots_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener function or method from property "clip_slots".
        """
        return

    def remove_color_index_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color_index".
        """
        return

    def remove_color_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color".
        """
        return

    def remove_is_triggered_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_triggered".
        """
        return

    def remove_name_listener(self, arg2: Callable) -> None:
        """
        Remove a previously set listener function or method from property "name".
        """
        return

    def set_fire_button_state(self, arg2: bool) -> None:
        """
        Set the scene's fire button state directly. Supports all launch modes.
        """
        return
