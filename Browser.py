# All referenced (missing descriptions)
from typing import Callable, Iterable
from Live.Base import Vector


class BrowserItem:
    """
    This class represents an item of the browser hierarchy.
    """
    @property
    def children(self) -> 'BrowserItemVector':
        """
        Const access to the descendants of this browser item.
        """
        return BrowserItemVector()

    @property
    def is_device(self) -> bool:
        """
        Indicates if the browser item represents a device.
        """
        return False

    @property
    def is_folder(self) -> bool:
        """
        Indicates if the browser item represents a folder.
        """
        return False

    @property
    def is_loadable(self) -> bool:
        """
        Indicates if the browser item can be loaded via the Browser's 'load_item' method.
        """
        return False

    @property
    def is_selected(self) -> bool:
        """
        Indicates if the browser item is selected.
        """
        return False

    @property
    def iter_children(self) -> 'BrowserItemIterator':
        """
        Const iterable access to the descendants of this browser item.
        """
        return BrowserItemIterator()

    @property
    def name(self) -> str:
        """
        Const access to the name of the browser item.
        """
        return ""

    @property
    def source(self) -> str:
        """
        Specifies where does item come from -- i.e. Live pack, user library...
        """
        return ""

    @property
    def uri(self) -> str:
        """
        The uri describes a unique identifier for a browser item.
        """
        return ""


class BrowserItemIterator(Iterable):
    """
    This class iterates over children of another BrowserItem.
    """

    def __iter__(self):
        return self

    def next(self) -> 'BrowserItemIterator':
        """
        Retrieve the next item.
        """
        return BrowserItemIterator()


class BrowserItemVector(Vector):
    def append(self, arg2: BrowserItem):
        return

    def extend(self, arg2: BrowserItem):
        return


class Relation:
    ancestor = None
    descendant = None
    equal = None
    parent = None


class FilterType:
    audio_effect_hotswap = None
    count = 0
    disabled = False
    drum_pad_hotswap = None
    hotswap_off = None
    instrument_hotswap = None
    midi_effect_hotswap = None
    midi_track_devices = None
    samples = None


class Browser:
    """
    This class represents the live browser database.
    """

    @property
    def _live_ptr(self) -> int:
        """
        :return: The pointer to the Live object.
        """
        return 0

    @property
    def audio_effects(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Audio Effects content.
        """
        return BrowserItem()

    @property
    def clips(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Clips content.
        """
        return BrowserItem()

    @property
    def colors(self) -> BrowserItemVector:
        """
        Returns a vector of browser items containing the configured colors.
        """
        return BrowserItemVector()

    @property
    def current_project(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Current Project content.
        """
        return BrowserItem()

    @property
    def drums(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Drums content.
        """
        return BrowserItem()

    @property
    def filter_type(self):
        """
        ???
        """
        return

    @property
    def hotswap_target(self) -> BrowserItem:
        """
        Bang triggered when the hotswap target has changed.
        """
        return BrowserItem()

    @property
    def instruments(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Instruments content.
        """
        return BrowserItem()

    @property
    def legacy_libraries(self) -> BrowserItemVector:
        """
        Returns a vector of browser items containing the installed legacy libraries. The vector is always empty as legacy library handling has been removed.
        """
        return BrowserItemVector()

    @property
    def max_for_live(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Max For Live content.
        """
        return BrowserItem()

    @property
    def midi_effects(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Midi Effects content.
        """
        return BrowserItem()

    @property
    def packs(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Packs content.
        """
        return BrowserItem()

    @property
    def plugins(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Plugins content.
        """
        return BrowserItem()

    @property
    def samples(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Samples content.
        """
        return BrowserItem()

    @property
    def sounds(self) -> BrowserItem:
        """
        Returns a browser item with access to all the Sounds content.
        """
        return BrowserItem()

    @property
    def user_folders(self) -> BrowserItemVector:
        """
        Returns a vector of browser items containing all the user folders.
        """
        return BrowserItemVector()

    @property
    def user_library(self) -> BrowserItem:
        """
        Returns a browser item with access to all the User Library content.
        """
        return BrowserItem()

    def add_filter_type_listener(self, arg2: Callable):
        """
        Add a listener callable object, which will be called as soon as the property "filter_type" has changed.
        """
        return

    def add_full_refresh_listener(self, arg2: Callable):
        """
        Add a listener callable object, which will be called as soon as the property "full_refresh" has changed.
        """
        return

    def add_hotswap_target_listener(self, arg2: Callable):
        """
        Add a listener callable object, which will be called as soon as the property "hotswap_target" has changed.
        """
        return

    def filter_type_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener callable object is connected to the property "filter_type".
        """
        return False

    def full_refresh_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener callable object is connected to the property "full_refresh".
        """
        return False

    def hotswap_target_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener callable object is connected to the property "hotswap_target".
        """
        return False

    def load_item(self, arg2: BrowserItem):
        """
        Loads the provided browser item.
        """
        return

    def preview_item(self, arg2: BrowserItem):
        """
        Previews the provided browser item.
        """
        return

    def relation_to_hotswap_target(self, arg2: BrowserItem) -> Relation:
        """
        Returns the relation between the given browser item and the current hotswap target.
        """
        return Relation()

    def remove_filter_type_listener(self, arg2: Callable):
        """
        Remove a previously set listener callable object from property "filter_type".
        """
        return

    def remove_full_refresh_listener(self, arg2: Callable):
        """
        Remove a previously set listener callable object from property "full_refresh".
        """
        return

    def remove_hotswap_target_listener(self, arg2: Callable):
        """
        Remove a previously set listener callable object from property "hotswap_target".
        """
        return

    def stop_preview(self):
        """
        Stop the current preview.
        """
        return
