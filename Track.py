# All referenced (missing descriptions)
from typing import Any, Callable
from typing_extensions import deprecated
from Live.Base import Vector
from Live.Clip import Clip
from Live.ClipSlot import ClipSlot
from Live.Device import Device


class DeviceContainer:
    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0


class DeviceInsertMode:
    count = None
    default = None
    selected_left = None
    selected_right = None


class RoutingChannelLayout:
    midi = None
    mono = None
    stereo = None


class RoutingChannel:
    @property
    def display_name(self) -> str:
        """
        Get the display name of the routing channel.
        """
        return ""

    @property
    def layout(self) -> RoutingChannelLayout:
        """
        Get the routing channel's Layout, e.g., mono or stereo.
        """
        return RoutingChannelLayout()


class RoutingChannelVector(Vector):
    def append(self, arg2: RoutingChannel) -> None:
        """
        Append a routing channel to the vector.
        """
        return


class RoutingTypeCategory:
    external = None
    internal = None
    master = None
    none = None
    parent_group_track = None
    resampling = None
    rewire = None
    track = None


class RoutingType:
    """
    This class represents a routing type.
    """
    @property
    def attached_object(self):
        """
        Live object associated with the routing type.
        """
        return Any()

    @property
    def category(self) -> RoutingTypeCategory:
        """
        Get the routing type's category.
        """
        return RoutingTypeCategory()

    @property
    def display_name(self) -> str:
        """
        Get the display name of the routing type.
        """
        return ""


class RoutingTypeVector(Vector):
    def append(self, arg2: RoutingType) -> None:
        """
        Append a routing type to the vector.
        """
        return


class Track:
    """
    This class represents a track in Live.
    It can be either an Audio track, a MIDI Track, a Return Track or the Master track.
    The Master Track and at least one Audio or MIDI track will be always present.
    Return Tracks are optional.
    """
    class monitoring_states:
        IN = None
        OFF = None
        AUTO = None

    class View:
        """
        Representing the view aspects of a Track.
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
            Get the canonical parent of the track view.
            """
            return Track()

        @property
        def device_insert_mode(self) -> DeviceInsertMode:
            """
            Get/Listen the device insertion mode of the track.
            """
            return DeviceInsertMode.default

        @property
        def is_collapsed(self) -> bool:
            """
            Get/Set/Listen if the track is shown collapsed in the arranger view.
            """
            return False

        @property
        def selected_device(self) -> Any:
            """
            Get/Set/Listen the insertion mode of the device. While in insertion mode, loading new devices from the browser will place devices at the selected position.
            """
            return Any()

        def add_device_insert_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "device_insert_mode" has changed.
            """
            return

        def add_is_collapsed_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
            """
            return

        def add_selected_device_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "selected_device" has changed.
            """
            return

        def device_insert_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "device_insert_mode".
            """
            return False

        def is_collapsed_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_collapsed".
            """
            return False

        def remove_device_insert_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "device_insert_mode".
            """
            return

        def remove_is_collapsed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_collapsed".
            """
            return

        def remove_selected_device_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "selected_device".
            """
            return

        def select_instrument(self) -> bool:
            """
            Selects the track's instrument if it has one.
            """
            return False

        def selected_device_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_device".
            """
            return False

    @property
    def _live_ptr(self) -> int:
        """
        :return: Pointer to the Live Object.
        """
        return 0

    @property
    def arm(self) -> bool:
        """
        Arm the track for recording. Not available for Master and Send Tracks.
        """
        return False

    @property
    def arrangement_clips(self) -> Vector[Clip]:
        """
        :return: Const access to the list of clips in arrangement view.
        The list will be empty for the master, send and group tracks.
        """
        return Vector()

    @property
    def available_input_routing_channels(self) -> RoutingChannelVector:
        """
        :return: List of available input routing channels.
        """
        return RoutingChannelVector()

    @property
    def available_input_routing_types(self) -> RoutingTypeVector:
        """
        :return: List of available input routing types.
        """
        return RoutingTypeVector()

    @property
    def available_output_routing_channels(self) -> RoutingChannelVector:
        """
        :return: List of available output routing channels.
        """
        return RoutingChannelVector()

    @property
    def available_output_routing_types(self) -> RoutingTypeVector:
        """
        :return: List of available output routing types.
        """
        return RoutingTypeVector()

    @property
    def can_be_armed(self) -> bool:
        """
        :return: True if the track can be armed.
        Not all tracks can be armed (for example return Tracks or the Master Tracks).
        """
        return False

    @property
    def can_be_frozen(self) -> bool:
        """
        :return: True if the track can be frozen.
        """
        return False

    @property
    def can_show_chains(self) -> bool:
        """
        :return: True if the track can show chains.
        """
        return False

    @property
    def canonical_parent(self):
        """
        :return: The track's canonical parent.
        """
        return

    @property
    def clip_slots(self) -> Vector[ClipSlot]:
        """
        :return: Const access to the list of clip slots.
        The list will be empty for the master and sendtracks.
        """
        return Vector()

    @property
    def color(self) -> int:
        """
        :return: Get/set access to the color of the Track (RGB).
        """
        return 0

    @property
    def color_index(self) -> int:
        """
        :return: Get/set access to the color index of the Track.
        """
        return 0

    @deprecated('Use Track.current_input_routing is deprecated since Live 9.7. Use Track.input_routing_type instead.')
    @property
    def current_input_routing(self) -> str:
        """
        :return: Get/Set the name of the current active input routing.When setting a new routing, the new routing must be one of the available ones.
        """
        return ''

    @deprecated('Use Track.current_input_sub_routing is deprecated since Live 9.7. Use Track.input_sub_routing_type instead.')
    @property
    def current_input_sub_routing(self) -> str:
        """
        :return: Get/Set the name of the current active input sub routing.When setting a new routing, the new routing must be one of the available ones.
        """
        return ''

    @deprecated('Use Track.current_monitoring_state is deprecated since Live 9.7. Use Track.monitoring_state instead.')
    @property
    def current_monitoring_state(self) -> int:
        """
        :return: Get/Set the current monitoring state.
        """
        return 0

    @deprecated('Use Track.current_output_routing is deprecated since Live 9.7. Use Track.output_routing_type instead.')
    @property
    def current_output_routing(self) -> str:
        """
        :return: Get/Set the name of the current active output routing.When setting a new routing, the new routing must be one of the available ones.
        """
        return ''

    @deprecated('Use Track.current_output_sub_routing is deprecated since Live 9.7. Use Track.output_sub_routing_type instead.')
    @property
    def current_output_sub_routing(self) -> str:
        """
        :return: Get/Set the name of the current active output sub routing.When setting a new routing, the new routing must be one of the available ones.
        """
        return ''

    @property
    def devices(self) -> Vector[Device]:
        """
        :return: Const access to all available Devices that are present in the TracksDevice chain.
        This tuple will also include the 'mixer_device' that every Track always has.
        """
        return Vector()

    @property
    def fired_slot_index(self) -> int:
        """
        :return: The index of the fired clip slot.
        This index is -1 if no slot is fired and -2 if the track's stop button has been fired.
        """
        return 0

    @property
    def fold_state(self) -> bool:
        """
        :return: Get/set the fold state of the track.
        Only if is_foldable is True.
        """
        return False

    @property
    def group_track(self):
        """
        :return: The group track if is_grouped.
        """
        return

    @property
    def has_audio_input(self) -> bool:
        """
        :return: Check if the track has an audio input.
        """
        return False

    @property
    def has_audio_output(self) -> bool:
        """
        :return: Check if the track has an audio output.
        """
        return False

    @property
    def has_midi_input(self) -> bool:
        """
        :return: Check if the track has a midi input.
        """
        return False

    @property
    def has_midi_output(self) -> bool:
        """
        :return: Check if the track has a midi output.
        """
        return False

    @property
    def implicit_arm(self) -> bool:
        """
        :return: Get/set the implicit arm status of the track.
        """
        return False

    @property
    def input_meter_left(self) -> float:
        """
        :return: The current level of the left input meter.
        From 0.0 to 1.0
        """
        return 0.0

    @property
    def input_meter_level(self) -> float:
        """
        :return: The current level of the input meter.
        From 0.0 to 1.0
        """
        return 0.0

    @property
    def input_meter_right(self) -> float:
        """
        :return: The current level of the right input meter.
        From 0.0 to 1.0
        """
        return 0.0

    @property
    def input_routing_channel(self) -> RoutingChannel:
        """
        :return: Get/Set the name of the current active input routing channel.
        When setting a new routing, the new routing must be one of the available ones.
        """
        return RoutingChannel()

    @property
    def input_routing_type(self) -> RoutingType:
        """
        :return: Get/Set the name of the current active input routing type.
        When setting a new routing, the new routing must be one of the available ones.
        """
        return RoutingType()

    @property
    def input_routings(self) -> Vector:
        """
        :return: Get the available input routings.
        """
        return Vector()

    @property
    def input_sub_routings(self) -> Vector:
        """
        :return: Get the available input sub routings.
        """
        return Vector()

    @property
    def is_foldable(self) -> bool:
        """
        :return: Check if the track can be folded.
        """
        return False

    @property
    def is_frozen(self) -> bool:
        """
        :return: Check if the track is frozen.
        """
        return False

    @property
    def is_grouped(self) -> bool:
        """
        :return: Check if the track is grouped.
        """
        return False

    @property
    def is_visible(self) -> bool:
        """
        :return: Check if the track is visible.
        """
        return False

    @property
    def mixer_device(self):
        """
        :return: The mixer device of the track.
        """
        return

    @property
    def mute(self) -> bool:
        """
        :return: Get/Set the mute status of the track.
        """
        return False

    @property
    def muted_via_solo(self) -> bool:
        """
        :return: If the track is muted because another track is soloed.
        """
        return False

    @property
    def name(self) -> str:
        """
        :return: Get/Set the name of the track.
        """
        return ""

    @property
    def output_meter_left(self) -> float:
        """
        :return: The current level of the left output meter.
        From 0.0 to 1.0
        """
        return 0.0

    @property
    def output_meter_level(self) -> float:
        """
        :return: The current level of the output meter.
        From 0.0 to 1.0
        """
        return 0.0

    @property
    def output_meter_right(self) -> float:
        """
        :return: The current level of the right output meter.
        From 0.0 to 1.0
        """
        return 0.0

    @property
    def output_routing_channel(self) -> RoutingChannel:
        """
        :return: Get/Set the name of the current active output routing channel.
        When setting a new routing, the new routing must be one of the available ones.
        """
        return RoutingChannel()

    @property
    def output_routing_type(self) -> RoutingType:
        """
        :return: Get/Set the name of the current active output routing type.
        When setting a new routing, the new routing must be one of the available ones.
        """
        return RoutingType()

    @deprecated("Track.output_routings is deprecated since Live 9.7. Please use Track.available_output_routing_types instead.")
    @property
    def output_routings(self) -> Vector:
        """
        :return: Get the available output routings.
        """
        return Vector()

    @deprecated("Track.output_sub_routings is deprecated since Live 9.7. Please use Track.available_output_routing_channels instead.")
    @property
    def output_sub_routings(self) -> Vector:
        """
        :return: Get the available output sub routings.
        """
        return Vector()

    @property
    def playing_slot_index(self) -> int:
        """
        :return: The index of the playing clip slot.
        This index is -1 if no slot is playing.
        """
        return 0

    @property
    def solo(self) -> bool:
        """
        :return: Get/Set the solo status of the track.
        That this will not disable the solo state of any other track.
        If you want exclusive solo, you have to disable the solo state of the other Tracks manually
        """
        return False

    @property
    def view(self) -> View:
        """
        :return: The view object for the track.
        """
        return self.View()

    def add_arm_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "arm" has changed.
        """
        return

    def add_arrangement_clips_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "arrangement_clips" has changed.
        """
        return

    def add_available_input_routing_channels_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_input_routing_channels" has changed.
        """
        return

    def add_available_input_routing_types_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_input_routing_types" has changed.
        """
        return

    def add_available_output_routing_channels_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_output_routing_channels" has changed.
        """
        return

    def add_available_output_routing_types_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "available_output_routing_types" has changed.
        """
        return
    
    def add_clip_slots_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "clip_slots" has changed.
        """
        return
    
    def add_color_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        return
    
    def add_color_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        return
    
    def add_current_input_routing_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "current_input_routing" has changed.
        """
        return
    
    def add_current_input_sub_routing_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "current_input_sub_routing" has changed.
        """
        return
    
    def add_current_monitoring_state_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "current_monitoring_state" has changed.
        """
        return
    
    def add_current_output_routing_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "current_output_routing" has changed.
        """
        return
    
    def add_current_output_sub_routing_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "current_output_sub_routing" has changed.
        """
        return
    
    def add_data_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "data" has changed.
        """
        return
    
    def add_devices_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "devices" has changed.
        """
        return
    
    def add_fired_slot_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "fired_slot_index" has changed.
        """
        return
    
    def add_has_audio_input_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_audio_input" has changed.
        """
        return
    
    def add_has_audio_output_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_audio_output" has changed.
        """
        return
    
    def add_has_midi_input_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_midi_input" has changed.
        """
        return
    
    def add_has_midi_output_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "has_midi_output" has changed.
        """
        return
    
    def add_implicit_arm_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "implicit_arm" has changed.
        """
        return
    
    def add_input_meter_left_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_meter_left" has changed.
        """
        return
    
    def add_input_meter_level_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_meter_level" has changed.
        """
        return
    
    def add_input_meter_right_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_meter_right" has changed.
        """
        return
    
    def add_input_routing_channel_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_routing_channel" has changed.
        """
        return
    
    def add_input_routing_type_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_routing_type" has changed.
        """
        return
    
    def add_input_routings_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_routings" has changed.
        """
        return
    
    def add_input_sub_routings_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "input_sub_routings" has changed.
        """
        return
    
    def add_is_frozen_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "is_frozen" has changed.
        """
        return
    
    def add_is_showing_chains_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "is_showing_chains" has changed.
        """
        return
    
    def add_mute_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "mute" has changed.
        """
        return
    
    def add_muted_via_solo_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
        """
        return
    
    def add_name_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        return
    
    def add_output_meter_left_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_meter_left" has changed.
        """
        return
    
    def add_output_meter_level_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_meter_level" has changed.
        """
        return
    
    def add_output_meter_right_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_meter_right" has changed.
        """
        return
    
    def add_output_routing_channel_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_routing_channel" has changed.
        """
        return
    
    def add_output_routing_type_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_routing_type" has changed.
        """
        return
    
    def add_output_routings_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_routings" has changed.
        """
        return
    
    def add_output_sub_routings_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "output_sub_routings" has changed.
        """
        return
    
    def add_playing_slot_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "playing_slot_index" has changed.
        """
        return
    
    def add_solo_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "solo" has changed.
        """
        return
    
    def arm_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "arm".
        """
        return False

    def arrangement_clips_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "arrangement_clips".
        """
        return False

    def available_input_routing_channels_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_input_routing_channels".
        """
        return False

    def available_input_routing_types_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_input_routing_types".
        """
        return False

    def available_output_routing_channels_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_output_routing_channels".
        """
        return False

    def available_output_routing_types_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "available_output_routing_types".
        """
        return False

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

    def current_input_routing_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "current_input_routing".
        """
        return False

    def current_input_sub_routing_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "current_input_sub_routing".
        """
        return False

    def current_monitoring_state_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "current_monitoring_state".
        """
        return False

    def current_output_routing_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "current_output_routing".
        """
        return False

    def current_output_sub_routing_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "current_output_sub_routing".
        """
        return False

    def data_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "data".
        """
        return False

    def delete_clip(self, arg2: Clip):
        """
        Delete the given clip from the track.
        Raises a runtime error when the clip belongs to another track.
        """
        return

    def delete_device(self, arg2: Device):
        """
        Delete the given device from the track.
        """
        return

    def devices_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "devices".
        """
        return False

    def duplicate_clip_slot(self, arg2: int) -> int:
        """
        Duplicate a clip and put it into the next free slot and return the index of the destination slot.
        A new scene is created if no free slot is available.
        If creating the new scene would exceed the limitations, a runtime error is raised.
        """
        return 0

    def duplicate_clip_to_arrangement(self, clip: Clip, destination_time: float) -> Clip:
        """
        Duplicate the given clip into the arrangement of this track at the provided destination time and return it.
        When the type of the clip and the type of the track are incompatible, a runtime error is raised.
        """
        return Clip()

    def fired_slot_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "fired_slot_index".
        """
        return False

    def get_data(self, key, default_value) -> object:
        """
        Get the data for the given key.
        """
        return object()

    def has_audio_input_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_audio_input".
        """
        return False

    def has_audio_output_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_audio_output".
        """
        return False

    def has_midi_input_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_midi_input".
        """
        return False

    def has_midi_output_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "has_midi_output".
        """
        return False

    def implicit_arm_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "implicit_arm".
        """
        return False

    def input_meter_left_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_meter_left".
        """
        return False

    def input_meter_level_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_meter_level".
        """
        return False

    def input_meter_right_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_meter_right".
        """
        return False

    def input_routing_channel_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_routing_channel".
        """
        return False

    def input_routing_type_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_routing_type".
        """
        return False

    def input_routings_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_routings".
        """
        return False

    def input_sub_routings_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "input_sub_routings".
        """
        return False

    def is_foldable_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_foldable".
        """
        return False

    def is_frozen_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_frozen".
        """
        return False

    def is_grouped_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_grouped".
        """
        return False

    def is_visible_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_visible".
        """
        return False

    def jump_in_running_session_clip(self, arg2: float):
        """
        Jump forward or backward in the currently running Session clip (if any) by the specified relative amount in beats.
        Does nothing if no Session Clip is currently running.
        """

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

    def output_meter_left_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_meter_left".
        """
        return False

    def output_meter_level_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_meter_level".
        """
        return False

    def output_meter_right_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_meter_right".
        """
        return False

    def output_routing_channel_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_routing_channel".
        """
        return False

    def output_routing_type_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_routing_type".
        """
        return False

    def output_routings_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_routings".
        """
        return False

    def output_sub_routings_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "output_sub_routings".
        """
        return False

    def playing_slot_index_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "playing_slot_index".
        """
        return False

    def remove_arm_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "arm".
        """
        return

    def remove_arrangement_clips_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "arrangement_clips".
        """
        return

    def remove_available_input_routing_channels_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_input_routing_channels".
        """
        return

    def remove_available_input_routing_types_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_input_routing_types".
        """
        return

    def remove_available_output_routing_channels_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_output_routing_channels".
        """
        return

    def remove_available_output_routing_types_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "available_output_routing_types".
        """
        return

    def remove_clip_slots_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "clip_slots".
        """
        return

    def remove_color_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "color_index".
        """
        return

    def remove_color_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "color".
        """
        return

    def remove_current_input_routing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "current_input_routing".
        """
        return

    def remove_current_input_sub_routing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "current_input_sub_routing".
        """
        return

    def remove_current_monitoring_state_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "current_monitoring_state".
        """
        return

    def remove_current_output_routing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "current_output_routing".
        """
        return

    def remove_current_output_sub_routing_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "current_output_sub_routing".
        """
        return

    def remove_data_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "data".
        """
        return

    def remove_devices_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "devices".
        """
        return

    def remove_fired_slot_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "fired_slot_index".
        """
        return

    def remove_has_audio_input_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_audio_input".
        """
        return

    def remove_has_audio_output_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_audio_output".
        """
        return

    def remove_has_midi_input_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_midi_input".
        """
        return

    def remove_has_midi_output_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "has_midi_output".
        """
        return

    def remove_implicit_arm_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "implicit_arm".
        """
        return

    def remove_input_meter_left_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_meter_left".
        """
        return

    def remove_input_meter_level_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_meter_level".
        """
        return

    def remove_input_meter_right_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_meter_right".
        """
        return

    def remove_input_routing_channel_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_routing_channel".
        """
        return

    def remove_input_routing_type_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_routing_type".
        """
        return

    def remove_input_routings_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_routings".
        """
        return

    def remove_input_sub_routings_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "input_sub_routings".
        """
        return

    def remove_is_frozen_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_frozen".
        """
        return

    def remove_is_showing_chains_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "is_showing_chains".
        """
        return

    def remove_mute_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "mute".
        """
        return

    def remove_muted_via_solo_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "muted_via_solo".
        """
        return

    def remove_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        return

    def remove_output_meter_left_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_meter_left".
        """
        return

    def remove_output_meter_level_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_meter_level".
        """
        return

    def remove_output_meter_right_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_meter_right".
        """
        return

    def remove_output_routing_channel_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_routing_channel".
        """
        return

    def remove_output_routing_type_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_routing_type".
        """
        return

    def remove_output_routings_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_routings".
        """
        return

    def remove_output_sub_routings_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "output_sub_routings".
        """
        return

    def remove_playing_slot_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "playing_slot_index".
        """
        return

    def remove_solo_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "solo".
        """
        return

    def set_data(self, key, value):
        """
        Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
        """
        return

    def solo_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "solo".
        """
        return False

    def stop_all_clips(self, quantized: bool = True):
        """
        Stop running and triggered clip and slots on this track.
        """
        return
