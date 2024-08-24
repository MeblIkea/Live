from typing import Any
from Live.Base import Vector
from Live.Device import Device
from Live.GroovePool import GroovePool
from Live.Scene import Scene
from Live.Track import Track


class CuePoint:
    @property
    def _live_ptr(self) -> int:
        """
        Get the pointer to the Live Object.
        """
        return 0

    @property
    def canonical_parent(self):
        """
        Get the canonical parent of the Cue Point.
        """
        return

    @property
    def name(self) -> str:
        """
        Get/Listen to the name of the Cue Point.
        """
        return ''

    @property
    def time(self) -> float:
        """
        Get/Listen to the Cue Point's time in beats.
        """
        return 0.0

    def add_name_listener(self, arg2: Any) -> None:
        """
        Add a listener to when the property "name" changes.
        """
        return

    def add_time_listener(self, arg2: Any) -> None:
        """
        Add a listener to when the property "time" changes.
        """
        return

    def jump(self) -> None:
        """
        When the Song is playing, set the playing-position quantized to this Cue point's time.
        When not playing, simply move the start playing position.
        """

    def name_has_listener(self, arg2: Any) -> bool:
        """
        Check if a listener is registered to the property "name"
        """
        return False

    def remove_name_listener(self, arg2: Any) -> None:
        """
        Remove a listener from the property "name"
        """
        return

    def remove_time_listener(self, arg2: Any) -> None:
        """
        Remove a listener from the property "time"
        """
        return

    def time_has_listener(self, arg2: Any) -> bool:
        """
        Check if a listener is registered to the property "time"
        """
        return False


class Song:
    class View:
        @property
        def _live_ptr(self) -> int:
            """
            Get the pointer to the Live Object.
            """
            return 0

        @property
        def canonical_parent(self):
            """
            Get the canonical parent of the song view.
            """
            return

        @property
        def detail_clip(self):
            """
            Get/Set the Clip that is currently visible in Live's Detail view.
            """
            return

        @property
        def draw_mode(self) -> bool:
            """
            Get/Set if the Envelope/Note draw mode is enabled.
            """
            return False

        @property
        def follow_song(self) -> bool:
            """
            Get/Set if the Arrangement view should scroll to show the play marker.
            """
            return False

        @property
        def highlighted_clip_slot(self):
            """
            Get/Set the clip slot, defined via the highlighted track and scene in the Session. Will be None for Master and Send tracks.
            """
            return

        @property
        def selected_chain(self):
            """
            Get the highlighted chain if available.
            """
            return

        @property
        def selected_parameter(self):
            """
            Get the currently selected device parameter.
            """
            return

        @property
        def selected_scene(self):
            """
            Get/Set the currently selected scene in Live's Session view.
            """
            return

        @property
        def selected_track(self):
            """
            Get/Set the currently selected Track in Live's Session or Arrangement view.
            """
            return

        def add_detail_clip_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "detail_clip" changes.
            """
            return

        def add_draw_mode_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "draw_mode" changes.
            """
            return

        def add_follow_song_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "follow_song" changes.
            """
            return

        def add_selected_chain_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_chain" changes.
            """
            return

        def add_selected_parameter_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_parameter" changes.
            """
            return

        def add_selected_scene_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_scene" changes.
            """
            return

        def add_selected_track_listener(self, arg2: Any) -> None:
            """
            Add a listener to when the property "selected_track" changes.
            """
            return

        def detail_clip_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "detail_clip"
            """
            return False

        def draw_mode_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "draw_mode"
            """
            return False

        def follow_song_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "follow_song"
            """
            return False

        def remove_detail_clip_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "detail_clip"
            """
            return

        def remove_draw_mode_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "draw_mode"
            """
            return

        def remove_follow_song_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "follow_song"
            """
            return

        def remove_selected_chain_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_chain"
            """
            return

        def remove_selected_parameter_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_parameter"
            """
            return

        def remove_selected_scene_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_scene"
            """
            return

        def remove_selected_track_listener(self, arg2: Any) -> None:
            """
            Remove a listener from the property "selected_track"
            """
            return

        def select_device(self, arg2: Device, ShouldAppointDevice: bool = True) -> None:
            """
            Select the given device.
            """
            return

        def selected_chain_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_chain"
            """
            return False

        def selected_parameter_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_parameter"
            """
            return False

        def selected_scene_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_scene"
            """
            return False

        def selected_track_has_listener(self, arg2: Any) -> bool:
            """
            Check if a listener is registered to the property "selected_track"
            """
            return False

    """
    <Method>Live.Song.Song.add_appointed_device_listener()<Description>Method</Description></Method>

    <Doc>	add_appointed_device_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "appointed_device" has changed. C++ signature :  void add_appointed_device_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_arrangement_overdub_listener()<Description>Method</Description></Method>

    <Doc>	add_arrangement_overdub_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "arrangement_overdub" has changed. C++ signature :  void add_arrangement_overdub_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_back_to_arranger_listener()<Description>Method</Description></Method>

    <Doc>	add_back_to_arranger_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "back_to_arranger" has changed. C++ signature :  void add_back_to_arranger_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_can_capture_midi_listener()<Description>Method</Description></Method>

    <Doc>	add_can_capture_midi_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "can_capture_midi" has changed. C++ signature :  void add_can_capture_midi_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_can_jump_to_next_cue_listener()<Description>Method</Description></Method>

    <Doc>	add_can_jump_to_next_cue_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "can_jump_to_next_cue" has changed. C++ signature :  void add_can_jump_to_next_cue_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_can_jump_to_prev_cue_listener()<Description>Method</Description></Method>

    <Doc>	add_can_jump_to_prev_cue_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "can_jump_to_prev_cue" has changed. C++ signature :  void add_can_jump_to_prev_cue_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_clip_trigger_quantization_listener()<Description>Method</Description></Method>

    <Doc>	add_clip_trigger_quantization_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "clip_trigger_quantization" has changed. C++ signature :  void add_clip_trigger_quantization_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_count_in_duration_listener()<Description>Method</Description></Method>

    <Doc>	add_count_in_duration_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "count_in_duration" has changed. C++ signature :  void add_count_in_duration_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_cue_points_listener()<Description>Method</Description></Method>

    <Doc>	add_cue_points_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "cue_points" has changed. C++ signature :  void add_cue_points_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_current_song_time_listener()<Description>Method</Description></Method>

    <Doc>	add_current_song_time_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "current_song_time" has changed. C++ signature :  void add_current_song_time_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_data_listener()<Description>Method</Description></Method>

    <Doc>	add_data_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "data" has changed. C++ signature :  void add_data_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_exclusive_arm_listener()<Description>Method</Description></Method>

    <Doc>	add_exclusive_arm_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "exclusive_arm" has changed. C++ signature :  void add_exclusive_arm_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_groove_amount_listener()<Description>Method</Description></Method>

    <Doc>	add_groove_amount_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "groove_amount" has changed. C++ signature :  void add_groove_amount_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_is_counting_in_listener()<Description>Method</Description></Method>

    <Doc>	add_is_counting_in_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "is_counting_in" has changed. C++ signature :  void add_is_counting_in_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_is_playing_listener()<Description>Method</Description></Method>

    <Doc>	add_is_playing_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "is_playing" has changed. C++ signature :  void add_is_playing_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_loop_length_listener()<Description>Method</Description></Method>

    <Doc>	add_loop_length_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "loop_length" has changed. C++ signature :  void add_loop_length_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_loop_listener()<Description>Method</Description></Method>

    <Doc>	add_loop_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "loop" has changed. C++ signature :  void add_loop_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_loop_start_listener()<Description>Method</Description></Method>

    <Doc>	add_loop_start_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "loop_start" has changed. C++ signature :  void add_loop_start_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_metronome_listener()<Description>Method</Description></Method>

    <Doc>	add_metronome_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "metronome" has changed. C++ signature :  void add_metronome_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_midi_recording_quantization_listener()<Description>Method</Description></Method>

    <Doc>	add_midi_recording_quantization_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "midi_recording_quantization" has changed. C++ signature :  void add_midi_recording_quantization_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_nudge_down_listener()<Description>Method</Description></Method>

    <Doc>	add_nudge_down_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "nudge_down" has changed. C++ signature :  void add_nudge_down_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_nudge_up_listener()<Description>Method</Description></Method>

    <Doc>	add_nudge_up_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "nudge_up" has changed. C++ signature :  void add_nudge_up_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_overdub_listener()<Description>Method</Description></Method>

    <Doc>	add_overdub_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "overdub" has changed. C++ signature :  void add_overdub_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_punch_in_listener()<Description>Method</Description></Method>

    <Doc>	add_punch_in_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "punch_in" has changed. C++ signature :  void add_punch_in_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_punch_out_listener()<Description>Method</Description></Method>

    <Doc>	add_punch_out_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "punch_out" has changed. C++ signature :  void add_punch_out_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_re_enable_automation_enabled_listener()<Description>Method</Description></Method>

    <Doc>	add_re_enable_automation_enabled_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "re_enable_automation_enabled" has changed. C++ signature :  void add_re_enable_automation_enabled_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_record_mode_listener()<Description>Method</Description></Method>

    <Doc>	add_record_mode_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "record_mode" has changed. C++ signature :  void add_record_mode_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_return_tracks_listener()<Description>Method</Description></Method>

    <Doc>	add_return_tracks_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "return_tracks" has changed. C++ signature :  void add_return_tracks_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_root_note_listener()<Description>Method</Description></Method>

    <Doc>	add_root_note_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "root_note" has changed. C++ signature :  void add_root_note_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_scale_intervals_listener()<Description>Method</Description></Method>

    <Doc>	add_scale_intervals_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "scale_intervals" has changed. C++ signature :  void add_scale_intervals_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_scale_name_listener()<Description>Method</Description></Method>

    <Doc>	add_scale_name_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "scale_name" has changed. C++ signature :  void add_scale_name_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_scenes_listener()<Description>Method</Description></Method>

    <Doc>	add_scenes_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "scenes" has changed. C++ signature :  void add_scenes_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_session_automation_record_listener()<Description>Method</Description></Method>

    <Doc>	add_session_automation_record_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "session_automation_record" has changed. C++ signature :  void add_session_automation_record_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_session_record_listener()<Description>Method</Description></Method>

    <Doc>	add_session_record_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "session_record" has changed. C++ signature :  void add_session_record_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_session_record_status_listener()<Description>Method</Description></Method>

    <Doc>	add_session_record_status_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "session_record_status" has changed. C++ signature :  void add_session_record_status_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_signature_denominator_listener()<Description>Method</Description></Method>

    <Doc>	add_signature_denominator_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "signature_denominator" has changed. C++ signature :  void add_signature_denominator_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_signature_numerator_listener()<Description>Method</Description></Method>

    <Doc>	add_signature_numerator_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "signature_numerator" has changed. C++ signature :  void add_signature_numerator_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_song_length_listener()<Description>Method</Description></Method>

    <Doc>	add_song_length_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "song_length" has changed. C++ signature :  void add_song_length_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_swing_amount_listener()<Description>Method</Description></Method>

    <Doc>	add_swing_amount_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "swing_amount" has changed. C++ signature :  void add_swing_amount_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_tempo_listener()<Description>Method</Description></Method>

    <Doc>	add_tempo_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "tempo" has changed. C++ signature :  void add_tempo_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_tracks_listener()<Description>Method</Description></Method>

    <Doc>	add_tracks_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "tracks" has changed. C++ signature :  void add_tracks_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.add_visible_tracks_listener()<Description>Method</Description></Method>

    <Doc>	add_visible_tracks_listener( (Song)arg1, (object)arg2) -&gt; None : Add a listener function or method, which will be called as soon as the property "visible_tracks" has changed. C++ signature :  void add_visible_tracks_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.appointed_device_has_listener()<Description>Method</Description></Method>

    <Doc>	appointed_device_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "appointed_device". C++ signature :  bool appointed_device_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.arrangement_overdub_has_listener()<Description>Method</Description></Method>

    <Doc>	arrangement_overdub_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "arrangement_overdub". C++ signature :  bool arrangement_overdub_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.back_to_arranger_has_listener()<Description>Method</Description></Method>

    <Doc>	back_to_arranger_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "back_to_arranger". C++ signature :  bool back_to_arranger_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.begin_undo_step()<Description>Method</Description></Method>

    <Doc>	begin_undo_step( (Song)arg1) -&gt; None : C++ signature :  void begin_undo_step(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.can_capture_midi_has_listener()<Description>Method</Description></Method>

    <Doc>	can_capture_midi_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "can_capture_midi". C++ signature :  bool can_capture_midi_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.can_jump_to_next_cue_has_listener()<Description>Method</Description></Method>

    <Doc>	can_jump_to_next_cue_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "can_jump_to_next_cue". C++ signature :  bool can_jump_to_next_cue_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.can_jump_to_prev_cue_has_listener()<Description>Method</Description></Method>

    <Doc>	can_jump_to_prev_cue_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "can_jump_to_prev_cue". C++ signature :  bool can_jump_to_prev_cue_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.capture_and_insert_scene()<Description>Method</Description></Method>

    <Doc>	capture_and_insert_scene( (Song)arg1 [, (int)CaptureMode=Song.CaptureMode.all]) -&gt; None : Capture currently playing clips and insert them as a new scene after the selected scene. Raises a runtime error if creating a new scene would exceed the limitations. C++ signature :  void capture_and_insert_scene(TPyHandle&lt;ASong&gt; [,int=Song.CaptureMode.all])</Doc>

    <Method>Live.Song.Song.capture_midi()<Description>Method</Description></Method>

    <Doc>	capture_midi( (Song)arg1 [, (int)Destination=Song.CaptureDestination.auto]) -&gt; None : Capture recently played MIDI material from audible tracks. If no Destination is given or Destination is set to CaptureDestination.auto, the captured material is inserted into the Session or Arrangement depending on which is visible. If Destination is set to CaptureDestination.session or CaptureDestination.arrangement, inserts the material into Session or Arrangement, respectively. Raises a limitation error when capturing into the Session and a new scene would have to be created but can't because it would exceed the limitations. C++ signature :  void capture_midi(TPyHandle&lt;ASong&gt; [,int=Song.CaptureDestination.auto])</Doc>

    <Method>Live.Song.Song.clip_trigger_quantization_has_listener()<Description>Method</Description></Method>

    <Doc>	clip_trigger_quantization_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "clip_trigger_quantization". C++ signature :  bool clip_trigger_quantization_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.continue_playing()<Description>Method</Description></Method>

    <Doc>	continue_playing( (Song)arg1) -&gt; None : Continue playing the song from the current position C++ signature :  void continue_playing(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.count_in_duration_has_listener()<Description>Method</Description></Method>

    <Doc>	count_in_duration_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "count_in_duration". C++ signature :  bool count_in_duration_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.create_audio_track()<Description>Method</Description></Method>

    <Doc>	create_audio_track( (Song)arg1 [, (object)Index=None]) -&gt; Track : Create a new audio track at the optional given index and return it.If the index is -1, the new track is added at the end. It will create a default audio track if possible. If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item C++ signature :  TWeakPtr&lt;TTrackPyHandle&gt; create_audio_track(TPyHandle&lt;ASong&gt; [,boost::python::api::object=None])</Doc>

    <Method>Live.Song.Song.create_midi_track()<Description>Method</Description></Method>

    <Doc>	create_midi_track( (Song)arg1 [, (object)Index=None]) -&gt; Track : Create a new midi track at the optional given index and return it.If the index is -1,  the new track is added at the end.It will create a default midi track if possible. If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item C++ signature :  TWeakPtr&lt;TTrackPyHandle&gt; create_midi_track(TPyHandle&lt;ASong&gt; [,boost::python::api::object=None])</Doc>

    <Method>Live.Song.Song.create_return_track()<Description>Method</Description></Method>

    <Doc>	create_return_track( (Song)arg1) -&gt; Track : Create a new return track at the end and return it. If the new track would exceed  the limitations, a limitation error is raised.  If the maximum number of return tracks is exceeded, a RuntimeError is raised. C++ signature :  TWeakPtr&lt;TTrackPyHandle&gt; create_return_track(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.create_scene()<Description>Method</Description></Method>

    <Doc>	create_scene( (Song)arg1, (int)arg2) -&gt; Scene : Create a new scene at the given index. If the index is -1, the new scene is added at the end. If the index is invalid or the new scene would exceed the limitations, a limitation error is raised. C++ signature :  TWeakPtr&lt;TPyHandle&lt;AScene&gt; &gt; create_scene(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.cue_points_has_listener()<Description>Method</Description></Method>

    <Doc>	cue_points_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "cue_points". C++ signature :  bool cue_points_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.current_song_time_has_listener()<Description>Method</Description></Method>

    <Doc>	current_song_time_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "current_song_time". C++ signature :  bool current_song_time_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.data_has_listener()<Description>Method</Description></Method>

    <Doc>	data_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "data". C++ signature :  bool data_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.delete_return_track()<Description>Method</Description></Method>

    <Doc>	delete_return_track( (Song)arg1, (int)arg2) -&gt; None : Delete the return track with the given index. If no track with this index exists, an exception will be raised. C++ signature :  void delete_return_track(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.delete_scene()<Description>Method</Description></Method>

    <Doc>	delete_scene( (Song)arg1, (int)arg2) -&gt; None : Delete the scene with the given index. If no scene with this index exists, an exception will be raised. C++ signature :  void delete_scene(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.delete_track()<Description>Method</Description></Method>

    <Doc>	delete_track( (Song)arg1, (int)arg2) -&gt; None : Delete the track with the given index. If no track with this index exists, an exception will be raised. C++ signature :  void delete_track(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.duplicate_scene()<Description>Method</Description></Method>

    <Doc>	duplicate_scene( (Song)arg1, (int)arg2) -&gt; None : Duplicates a scene and selects the new one. Raises a limitation error if creating a new scene would exceed the limitations. C++ signature :  void duplicate_scene(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.duplicate_track()<Description>Method</Description></Method>

    <Doc>	duplicate_track( (Song)arg1, (int)arg2) -&gt; None : Duplicates a track and selects the new one. If the track is inside a folded group track, the group track is unfolded. Raises a limitation error if creating a new track would exceed the limitations. C++ signature :  void duplicate_track(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.end_undo_step()<Description>Method</Description></Method>

    <Doc>	end_undo_step( (Song)arg1) -&gt; None : C++ signature :  void end_undo_step(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.exclusive_arm_has_listener()<Description>Method</Description></Method>

    <Doc>	exclusive_arm_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "exclusive_arm". C++ signature :  bool exclusive_arm_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.find_device_position()<Description>Method</Description></Method>

    <Doc>	find_device_position( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -&gt; int : Returns the closest possible position to the given target, where the device can be inserted. If inserting is not possible at all (i.e. if the device type is wrong), -1 is returned. C++ signature :  int find_device_position(TPyHandle&lt;ASong&gt;,TPyHandle&lt;ADevice&gt;,TPyHandleBase,int)</Doc>

    <Method>Live.Song.Song.force_link_beat_time()<Description>Method</Description></Method>

    <Doc>	force_link_beat_time( (Song)arg1) -&gt; None : Force the Link timeline to jump to Lives current beat time. Danger: This can cause beat time discontinuities in other connected apps. C++ signature :  void force_link_beat_time(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.get_beats_loop_length()<Description>Method</Description></Method>

    <Doc>	get_beats_loop_length( (Song)arg1) -&gt; BeatTime : Get const access to the songs loop length, using a BeatTime class with the current global set signature. C++ signature :  NSongApi::TBeatTime get_beats_loop_length(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.get_beats_loop_start()<Description>Method</Description></Method>

    <Doc>	get_beats_loop_start( (Song)arg1) -&gt; BeatTime : Get const access to the songs loop start, using a BeatTime class with the current global set signature. C++ signature :  NSongApi::TBeatTime get_beats_loop_start(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.get_current_beats_song_time()<Description>Method</Description></Method>

    <Doc>	get_current_beats_song_time( (Song)arg1) -&gt; BeatTime : Get const access to the songs current playing position, using a BeatTime class with the current global set signature. C++ signature :  NSongApi::TBeatTime get_current_beats_song_time(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.get_current_smpte_song_time()<Description>Method</Description></Method>

    <Doc>	get_current_smpte_song_time( (Song)arg1, (int)arg2) -&gt; SmptTime : Get const access to the songs current playing position, by specifying the SMPTE format in which you would like to receive the time. C++ signature :  NSongApi::TSmptTime get_current_smpte_song_time(TPyHandle&lt;ASong&gt;,int)</Doc>

    <Method>Live.Song.Song.get_data()<Description>Method</Description></Method>

    <Doc>	get_data( (Song)arg1, (object)key, (object)default_value) -&gt; object : Get data for the given key, that was previously stored using set_data. C++ signature :  boost::python::api::object get_data(TPyHandle&lt;ASong&gt;,TString,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.groove_amount_has_listener()<Description>Method</Description></Method>

    <Doc>	groove_amount_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "groove_amount". C++ signature :  bool groove_amount_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.is_counting_in_has_listener()<Description>Method</Description></Method>

    <Doc>	is_counting_in_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "is_counting_in". C++ signature :  bool is_counting_in_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.is_cue_point_selected()<Description>Method</Description></Method>

    <Doc>	is_cue_point_selected( (Song)arg1) -&gt; bool : Return true if the global playing pos is currently on a cue point. C++ signature :  bool is_cue_point_selected(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.is_playing_has_listener()<Description>Method</Description></Method>

    <Doc>	is_playing_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "is_playing". C++ signature :  bool is_playing_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.jump_by()<Description>Method</Description></Method>

    <Doc>	jump_by( (Song)arg1, (float)arg2) -&gt; None : Set a new playing pos, relative to the current one. C++ signature :  void jump_by(TPyHandle&lt;ASong&gt;,double)</Doc>

    <Method>Live.Song.Song.jump_to_next_cue()<Description>Method</Description></Method>

    <Doc>	jump_to_next_cue( (Song)arg1) -&gt; None : Jump to the next cue (marker) if possible. C++ signature :  void jump_to_next_cue(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.jump_to_prev_cue()<Description>Method</Description></Method>

    <Doc>	jump_to_prev_cue( (Song)arg1) -&gt; None : Jump to the prior cue (marker) if possible. C++ signature :  void jump_to_prev_cue(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.loop_has_listener()<Description>Method</Description></Method>

    <Doc>	loop_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "loop". C++ signature :  bool loop_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.loop_length_has_listener()<Description>Method</Description></Method>

    <Doc>	loop_length_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "loop_length". C++ signature :  bool loop_length_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.loop_start_has_listener()<Description>Method</Description></Method>

    <Doc>	loop_start_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "loop_start". C++ signature :  bool loop_start_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.metronome_has_listener()<Description>Method</Description></Method>

    <Doc>	metronome_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "metronome". C++ signature :  bool metronome_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.midi_recording_quantization_has_listener()<Description>Method</Description></Method>

    <Doc>	midi_recording_quantization_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "midi_recording_quantization". C++ signature :  bool midi_recording_quantization_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.move_device()<Description>Method</Description></Method>

    <Doc>	move_device( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -&gt; int : Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen. If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to. C++ signature :  int move_device(TPyHandle&lt;ASong&gt;,TPyHandle&lt;ADevice&gt;,TPyHandleBase,int)</Doc>

    <Method>Live.Song.Song.nudge_down_has_listener()<Description>Method</Description></Method>

    <Doc>	nudge_down_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "nudge_down". C++ signature :  bool nudge_down_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.nudge_up_has_listener()<Description>Method</Description></Method>

    <Doc>	nudge_up_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "nudge_up". C++ signature :  bool nudge_up_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.overdub_has_listener()<Description>Method</Description></Method>

    <Doc>	overdub_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "overdub". C++ signature :  bool overdub_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.play_selection()<Description>Method</Description></Method>

    <Doc>	play_selection( (Song)arg1) -&gt; None : Start playing the current set selection, or do nothing if no selection is set. C++ signature :  void play_selection(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.punch_in_has_listener()<Description>Method</Description></Method>

    <Doc>	punch_in_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "punch_in". C++ signature :  bool punch_in_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.punch_out_has_listener()<Description>Method</Description></Method>

    <Doc>	punch_out_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "punch_out". C++ signature :  bool punch_out_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.re_enable_automation()<Description>Method</Description></Method>

    <Doc>	re_enable_automation( (Song)arg1) -&gt; None : Discards overrides of automated parameters. C++ signature :  void re_enable_automation(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.re_enable_automation_enabled_has_listener()<Description>Method</Description></Method>

    <Doc>	re_enable_automation_enabled_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "re_enable_automation_enabled". C++ signature :  bool re_enable_automation_enabled_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.record_mode_has_listener()<Description>Method</Description></Method>

    <Doc>	record_mode_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "record_mode". C++ signature :  bool record_mode_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.redo()<Description>Method</Description></Method>

    <Doc>	redo( (Song)arg1) -&gt; None : Redo the last action that was undone. C++ signature :  void redo(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.remove_appointed_device_listener()<Description>Method</Description></Method>

    <Doc>	remove_appointed_device_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "appointed_device". C++ signature :  void remove_appointed_device_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_arrangement_overdub_listener()<Description>Method</Description></Method>

    <Doc>	remove_arrangement_overdub_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "arrangement_overdub". C++ signature :  void remove_arrangement_overdub_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_back_to_arranger_listener()<Description>Method</Description></Method>

    <Doc>	remove_back_to_arranger_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "back_to_arranger". C++ signature :  void remove_back_to_arranger_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_can_capture_midi_listener()<Description>Method</Description></Method>

    <Doc>	remove_can_capture_midi_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "can_capture_midi". C++ signature :  void remove_can_capture_midi_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_can_jump_to_next_cue_listener()<Description>Method</Description></Method>

    <Doc>	remove_can_jump_to_next_cue_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "can_jump_to_next_cue". C++ signature :  void remove_can_jump_to_next_cue_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_can_jump_to_prev_cue_listener()<Description>Method</Description></Method>

    <Doc>	remove_can_jump_to_prev_cue_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "can_jump_to_prev_cue". C++ signature :  void remove_can_jump_to_prev_cue_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_clip_trigger_quantization_listener()<Description>Method</Description></Method>

    <Doc>	remove_clip_trigger_quantization_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "clip_trigger_quantization". C++ signature :  void remove_clip_trigger_quantization_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_count_in_duration_listener()<Description>Method</Description></Method>

    <Doc>	remove_count_in_duration_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "count_in_duration". C++ signature :  void remove_count_in_duration_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_cue_points_listener()<Description>Method</Description></Method>

    <Doc>	remove_cue_points_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "cue_points". C++ signature :  void remove_cue_points_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_current_song_time_listener()<Description>Method</Description></Method>

    <Doc>	remove_current_song_time_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "current_song_time". C++ signature :  void remove_current_song_time_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_data_listener()<Description>Method</Description></Method>

    <Doc>	remove_data_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "data". C++ signature :  void remove_data_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_exclusive_arm_listener()<Description>Method</Description></Method>

    <Doc>	remove_exclusive_arm_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "exclusive_arm". C++ signature :  void remove_exclusive_arm_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_groove_amount_listener()<Description>Method</Description></Method>

    <Doc>	remove_groove_amount_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "groove_amount". C++ signature :  void remove_groove_amount_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_is_counting_in_listener()<Description>Method</Description></Method>

    <Doc>	remove_is_counting_in_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "is_counting_in". C++ signature :  void remove_is_counting_in_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_is_playing_listener()<Description>Method</Description></Method>

    <Doc>	remove_is_playing_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "is_playing". C++ signature :  void remove_is_playing_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_loop_length_listener()<Description>Method</Description></Method>

    <Doc>	remove_loop_length_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "loop_length". C++ signature :  void remove_loop_length_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_loop_listener()<Description>Method</Description></Method>

    <Doc>	remove_loop_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "loop". C++ signature :  void remove_loop_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_loop_start_listener()<Description>Method</Description></Method>

    <Doc>	remove_loop_start_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "loop_start". C++ signature :  void remove_loop_start_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_metronome_listener()<Description>Method</Description></Method>

    <Doc>	remove_metronome_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "metronome". C++ signature :  void remove_metronome_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_midi_recording_quantization_listener()<Description>Method</Description></Method>

    <Doc>	remove_midi_recording_quantization_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "midi_recording_quantization". C++ signature :  void remove_midi_recording_quantization_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_nudge_down_listener()<Description>Method</Description></Method>

    <Doc>	remove_nudge_down_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "nudge_down". C++ signature :  void remove_nudge_down_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_nudge_up_listener()<Description>Method</Description></Method>

    <Doc>	remove_nudge_up_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "nudge_up". C++ signature :  void remove_nudge_up_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_overdub_listener()<Description>Method</Description></Method>

    <Doc>	remove_overdub_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "overdub". C++ signature :  void remove_overdub_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_punch_in_listener()<Description>Method</Description></Method>

    <Doc>	remove_punch_in_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "punch_in". C++ signature :  void remove_punch_in_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_punch_out_listener()<Description>Method</Description></Method>

    <Doc>	remove_punch_out_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "punch_out". C++ signature :  void remove_punch_out_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_re_enable_automation_enabled_listener()<Description>Method</Description></Method>

    <Doc>	remove_re_enable_automation_enabled_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "re_enable_automation_enabled". C++ signature :  void remove_re_enable_automation_enabled_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_record_mode_listener()<Description>Method</Description></Method>

    <Doc>	remove_record_mode_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "record_mode". C++ signature :  void remove_record_mode_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_return_tracks_listener()<Description>Method</Description></Method>

    <Doc>	remove_return_tracks_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "return_tracks". C++ signature :  void remove_return_tracks_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_root_note_listener()<Description>Method</Description></Method>

    <Doc>	remove_root_note_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "root_note". C++ signature :  void remove_root_note_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_scale_intervals_listener()<Description>Method</Description></Method>

    <Doc>	remove_scale_intervals_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "scale_intervals". C++ signature :  void remove_scale_intervals_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_scale_name_listener()<Description>Method</Description></Method>

    <Doc>	remove_scale_name_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "scale_name". C++ signature :  void remove_scale_name_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_scenes_listener()<Description>Method</Description></Method>

    <Doc>	remove_scenes_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "scenes". C++ signature :  void remove_scenes_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_session_automation_record_listener()<Description>Method</Description></Method>

    <Doc>	remove_session_automation_record_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "session_automation_record". C++ signature :  void remove_session_automation_record_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_session_record_listener()<Description>Method</Description></Method>

    <Doc>	remove_session_record_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "session_record". C++ signature :  void remove_session_record_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_session_record_status_listener()<Description>Method</Description></Method>

    <Doc>	remove_session_record_status_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "session_record_status". C++ signature :  void remove_session_record_status_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_signature_denominator_listener()<Description>Method</Description></Method>

    <Doc>	remove_signature_denominator_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "signature_denominator". C++ signature :  void remove_signature_denominator_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_signature_numerator_listener()<Description>Method</Description></Method>

    <Doc>	remove_signature_numerator_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "signature_numerator". C++ signature :  void remove_signature_numerator_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_song_length_listener()<Description>Method</Description></Method>

    <Doc>	remove_song_length_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "song_length". C++ signature :  void remove_song_length_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_swing_amount_listener()<Description>Method</Description></Method>

    <Doc>	remove_swing_amount_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "swing_amount". C++ signature :  void remove_swing_amount_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_tempo_listener()<Description>Method</Description></Method>

    <Doc>	remove_tempo_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "tempo". C++ signature :  void remove_tempo_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_tracks_listener()<Description>Method</Description></Method>

    <Doc>	remove_tracks_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "tracks". C++ signature :  void remove_tracks_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.remove_visible_tracks_listener()<Description>Method</Description></Method>

    <Doc>	remove_visible_tracks_listener( (Song)arg1, (object)arg2) -&gt; None : Remove a previously set listener function or method from property "visible_tracks". C++ signature :  void remove_visible_tracks_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.return_tracks_has_listener()<Description>Method</Description></Method>

    <Doc>	return_tracks_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "return_tracks". C++ signature :  bool return_tracks_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.root_note_has_listener()<Description>Method</Description></Method>

    <Doc>	root_note_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "root_note". C++ signature :  bool root_note_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.scale_intervals_has_listener()<Description>Method</Description></Method>

    <Doc>	scale_intervals_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "scale_intervals". C++ signature :  bool scale_intervals_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.scale_name_has_listener()<Description>Method</Description></Method>

    <Doc>	scale_name_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "scale_name". C++ signature :  bool scale_name_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.scenes_has_listener()<Description>Method</Description></Method>

    <Doc>	scenes_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "scenes". C++ signature :  bool scenes_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.scrub_by()<Description>Method</Description></Method>

    <Doc>	scrub_by( (Song)arg1, (float)arg2) -&gt; None : Same as jump_by, but does not stop playback. C++ signature :  void scrub_by(TPyHandle&lt;ASong&gt;,double)</Doc>

    <Method>Live.Song.Song.session_automation_record_has_listener()<Description>Method</Description></Method>

    <Doc>	session_automation_record_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "session_automation_record". C++ signature :  bool session_automation_record_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.session_record_has_listener()<Description>Method</Description></Method>

    <Doc>	session_record_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "session_record". C++ signature :  bool session_record_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.session_record_status_has_listener()<Description>Method</Description></Method>

    <Doc>	session_record_status_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "session_record_status". C++ signature :  bool session_record_status_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.set_data()<Description>Method</Description></Method>

    <Doc>	set_data( (Song)arg1, (object)key, (object)value) -&gt; None : Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set. C++ signature :  void set_data(TPyHandle&lt;ASong&gt;,TString,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.set_or_delete_cue()<Description>Method</Description></Method>

    <Doc>	set_or_delete_cue( (Song)arg1) -&gt; None : When a cue is selected, it gets deleted. If no cue is selected, a new cue is created at the current global songtime. C++ signature :  void set_or_delete_cue(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.signature_denominator_has_listener()<Description>Method</Description></Method>

    <Doc>	signature_denominator_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "signature_denominator". C++ signature :  bool signature_denominator_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.signature_numerator_has_listener()<Description>Method</Description></Method>

    <Doc>	signature_numerator_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "signature_numerator". C++ signature :  bool signature_numerator_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.song_length_has_listener()<Description>Method</Description></Method>

    <Doc>	song_length_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "song_length". C++ signature :  bool song_length_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.start_playing()<Description>Method</Description></Method>

    <Doc>	start_playing( (Song)arg1) -&gt; None : Start playing from the startmarker C++ signature :  void start_playing(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.stop_all_clips()<Description>Method</Description></Method>

    <Doc>	stop_all_clips( (Song)arg1 [, (bool)Quantized=True]) -&gt; None : Stop all playing Clips (if any) but continue playing the Song. C++ signature :  void stop_all_clips(TPyHandle&lt;ASong&gt; [,bool=True])</Doc>

    <Method>Live.Song.Song.stop_playing()<Description>Method</Description></Method>

    <Doc>	stop_playing( (Song)arg1) -&gt; None : Stop playing the Song. C++ signature :  void stop_playing(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.swing_amount_has_listener()<Description>Method</Description></Method>

    <Doc>	swing_amount_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "swing_amount". C++ signature :  bool swing_amount_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.tap_tempo()<Description>Method</Description></Method>

    <Doc>	tap_tempo( (Song)arg1) -&gt; None : Trigger the tap tempo function. C++ signature :  void tap_tempo(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.tempo_has_listener()<Description>Method</Description></Method>

    <Doc>	tempo_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "tempo". C++ signature :  bool tempo_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.tracks_has_listener()<Description>Method</Description></Method>

    <Doc>	tracks_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "tracks". C++ signature :  bool tracks_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>

    <Method>Live.Song.Song.trigger_session_record()<Description>Method</Description></Method>

    <Doc>	trigger_session_record( (Song)self [, (float)record_length=1.7976931348623157e+308]) -&gt; None : Triggers a new session recording. C++ signature :  void trigger_session_record(TPyHandle&lt;ASong&gt; [,double=1.7976931348623157e+308])</Doc>

    <Method>Live.Song.Song.undo()<Description>Method</Description></Method>

    <Doc>	undo( (Song)arg1) -&gt; None : Undo the last action that was made. C++ signature :  void undo(TPyHandle&lt;ASong&gt;)</Doc>

    <Method>Live.Song.Song.visible_tracks_has_listener()<Description>Method</Description></Method>

    <Doc>	visible_tracks_has_listener( (Song)arg1, (object)arg2) -&gt; bool : Returns true, if the given listener function or method is connected to the property "visible_tracks". C++ signature :  bool visible_tracks_has_listener(TPyHandle&lt;ASong&gt;,boost::python::api::object)</Doc>
    """

    @property
    def _live_ptr(self) -> int:
        """
        :return: The pointer to the Live object.
        """
        return 0

    @property
    def appointed_device(self) -> 'Device':
        """
        Read, write and listen access to the currently appointed device.
        """
        return Device()

    @property
    def arrangement_overdub(self) -> bool:
        """
        Get/Set the global arrangement overdub state.
        """
        return False

    @property
    def back_to_arranger(self) -> bool:
        """
        Get/Set if triggering a Clip in the Session, disabled the playback of Clips in the Arranger.
        """
        return False

    @property
    def can_capture_midi(self) -> bool:
        """
        Get whether there currently is material to be captured on any tracks.
        """
        return False

    @property
    def can_jump_to_next_cue(self) -> bool:
        """
        Get whether it is possible to jump to the next cue.
        """
        return False

    @property
    def can_jump_to_prev_cue(self) -> bool:
        """
        Get whether it is possible to jump to the previous cue.
        """
        return False

    @property
    def can_redo(self) -> bool:
        """
        Get whether it is possible to redo the last action.
        """
        return False

    @property
    def can_undo(self) -> bool:
        """
        Get whether it is possible to undo the last action.
        """
        return False

    @property
    def canonical_parent(self):
        """
        Get the canonical parent of the object.
        """
        return None

    @property
    def clip_trigger_quantization(self) -> int:
        """
        Get/Set the global Clip trigger quantization.
        """
        return 0

    @property
    def count_in_duration(self) -> int:
        """
        Get the count in duration. Returns an index, mapped as follows: 0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.
        """
        return 0

    @property
    def cue_points(self) -> Vector:
        """
        Get the cue points in the song.
        """
        return Vector()

    @property
    def current_song_time(self) -> float:
        """
        Get the current song time in beats.
        """
        return 0.0

    @property
    def exclusive_arm(self) -> bool:
        """
        Get if Tracks should be armed exclusively by default.
        """
        return False

    @property
    def exclusive_solo(self) -> bool:
        """
        Get if Tracks should be soloed exclusively by default.
        """
        return False

    @property
    def groove_amount(self) -> float:
        """
        Get/Set the global groove amount.
        """
        return 0.0

    @property
    def groove_pool(self) -> 'GroovePool':
        """
        Get the groove pool.
        """
        return GroovePool()

    @property
    def is_counting_in(self) -> bool:
        """
        Get whether the song is currently counting in.
        """
        return False

    @property
    def is_playing(self) -> bool:
        """
        Get whether the song is currently playing.
        """
        return False

    @property
    def last_event_time(self) -> float:
        """
        Get the time of the last event.
        """
        return 0.0

    @property
    def loop(self) -> bool:
        """
        Get/Set the looping flag that en/disables the usage of the globalloop markers in the song.
        """
        return False

    @property
    def loop_length(self) -> float:
        """
        Get/Set the length of the global loop marker position in beats.
        """
        return 0.0

    @property
    def loop_start(self) -> float:
        """
        Get/Set the start of the global loop marker position in beats.
        """
        return 0.0

    @property
    def master_track(self) -> 'Track':
        """
        Get the master track.
        """
        return Track()

    @property
    def metronome(self) -> bool:
        """
        Get/Set the metronome state.
        """
        return False

    @property
    def midi_recording_quantization(self) -> int:
        """
        Get/Set the global MIDI recording quantization.
        """
        return 0

    @property
    def nudge_down(self) -> bool:
        """
        Get/Set the nudge down state.
        """
        return False

    @property
    def nudge_up(self) -> bool:
        """
        Get/Set the nudge up state.
        """
        return False

    @property
    def overdub(self) -> bool:
        """
        Legacy hook for Live 8 overdub state. Now hooks to session record, but never starts playback.
        """
        return False

    @property
    def punch_in(self) -> bool:
        """
        Get/Set the global punch in state.
        """
        return False

    @property
    def punch_out(self) -> bool:
        """
        Get/Set the global punch out state.
        """
        return False

    @property
    def re_enable_automation_enabled(self) -> bool:
        """
        Get/Set the re-enable automation state.
        """
        return False

    @property
    def record_mode(self) -> int:
        """
        Get/Set the record mode.
        """
        return 0

    @property
    def return_tracks(self) -> Vector[Track]:
        """
        Get the return tracks.
        """
        return Vector()

    @property
    def root_note(self) -> int:
        """
        Set and access the root note (i.e. key) of the song used for control surfaces. The root note can be a number between 0 and 11, with 0 corresponding to C and 11 corresponding to B.
        """
        return 0

    @property
    def scale_intervals(self) -> list[int]:
        """
        Reports the current scale's intervals as a list of integers, starting with the root note and representing the number of half steps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)
        """
        return []

    @property
    def scale_name(self) -> str:
        """
        Reports the current scale's name.
        """
        return ''

    @property
    def scenes(self) -> Vector[Scene]:
        """
        Get the scenes.
        """
        return Vector()

    @property
    def select_on_launch(self) -> bool:
        """
        Get if Scenes and Clips should be selected when fired.
        """
        return False

    @property
    def session_automation_record(self) -> bool:
        """
        Get the session automation record state.
        """
        return False

    @property
    def session_record(self) -> bool:
        """
        Get the session record state.
        """
        return False

    @property
    def session_record_status(self) -> int:
        """
        Get the session slot-recording state.
        """
        return 0

    @property
    def signature_denominator(self) -> int:
        """
        Get/Set the global time signature denominator.
        """
        return 0

    @property
    def signature_numerator(self) -> int:
        """
        Get/Set the global time signature numerator.
        """
        return 0

    @property
    def song_length(self) -> float:
        """
        Get the song length in beats.
        """
        return 0.0

    @property
    def swing_amount(self) -> float:
        """
        Get/Set the global swing amount.
        """
        return 0.0

    @property
    def tempo(self) -> float:
        """
        Get/Set the global tempo.
        """
        return 0.0

    @property
    def tracks(self) -> Vector[Track]:
        """
        Get the tracks.
        """
        return Vector()

    @property
    def view(self) -> 'Song.View':
        """
        Get the view object.
        """
        return Song.View()

    @property
    def visible_tracks(self) -> Vector[Track]:
        """
        Get the visible tracks.
        """
        return Vector()

