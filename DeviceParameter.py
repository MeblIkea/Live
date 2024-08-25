# All referenced (missing descriptions)
from typing import Callable


class AutomationState:
    none = None
    overridden = None
    playing = None


class ParameterState:
    disabled = None
    enabled = None
    irrelevant = None


class DeviceParameter:
    """
    This class represents an (automatable) parameter within a MIDI orAudio DSP-Device.
    """
    @property
    def _live_ptr(self) -> int:
        """
        :return: Get the pointer to the Live Object.
        """
        return 0

    @property
    def automation_state(self) -> AutomationState:
        """
        :return: Returns state of type AutomationState.
        """
        return AutomationState()

    @property
    def canonical_parent(self):
        """
        :return: Get the canonical parent of the Device.View.
        """
        return None

    @property
    def default_value(self):
        """
        :return: Return the default value for this parameter.
        A Default value is only available for non-quantized parameter types (see 'is_quantized').
        """
        return

    @property
    def is_enabled(self) -> bool:
        """
        :return: Returns false if the parameter has been macro mapped or disabled by Max.
        """
        return False

    @property
    def is_quantized(self) -> bool:
        """
        :return: Returns True, if this value is a boolean or integer like switch.
        Non quantized values are continues float values.
        """
        return False

    @property
    def max(self) -> float:
        """
        :return: Returns const access to the upper value of the allowed range for this parameter.
        """
        return 0.0

    @property
    def min(self) -> float:
        """
        :return: Returns const access to the lower value of the allowed range for this parameter.
        """
        return 0.0

    @property
    def name(self) -> str:
        """
        :return: Returns const access the name of this parameter, as visible in Lives automation choosers.
        """
        return ""

    @property
    def original_name(self) -> str:
        """
        :return: Returns const access the original name of this parameter, unaffected of any renamings.
        """
        return ""

    @property
    def state(self) -> ParameterState:
        """
        :return: Returns the state of the parameter:
        - enabled - the parameter's value can be changed,
        - irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled,
        - disabled - the parameter's value cannot be changed.
        """
        return ParameterState()

    @property
    def value(self):
        """
        :return: Get/Set the current value (as visible in the GUI) this parameter.
        The value must be inside the min/max properties of this device.
        """
        return

    @property
    def value_items(self):
        """
        :return: Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False.
        """
        return

    def add_automation_state_listener(self, arg1: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "automation_state" has changed.
        """
        return

    def add_name_listener(self, arg1: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        return

    def add_state_listener(self, arg1: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "state" has changed.
        """
        return

    def add_value_listener(self, arg1: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "value" has changed.
        """
        return

    def automation_state_has_listener(self, arg1: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "automation_state".
        """
        return False

    def begin_gesture(self):
        """
        Notify the beginning of a modification of the parameter,
        when a sequence of modifications has to be considered a consistent group --
        for example, when recording automation.
        """
        return

    def end_gesture(self):
        """
        Notify the end of a modification of the parameter. See begin_gesture.
        """
        return

    def name_has_listener(self, arg1: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        return False

    def re_enable_automation(self):
        """
        Re-enable automation for this parameter.
        """
        return

    def remove_automation_state_listener(self, arg1: Callable):
        """
        Remove a previously set listener function or method from property "automation_state".
        """
        return

    def remove_name_listener(self, arg1: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        return

    def remove_state_listener(self, arg1: Callable):
        """
        Remove a previously set listener function or method from property "state".
        """
        return

    def remove_value_listener(self, arg1: Callable):
        """
        Remove a previously set listener function or method from property "value".
        """
        return

    def state_has_listener(self, arg1: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "state".
        """
        return False

    def str_for_value(self, arg1: float) -> str:
        """
        Return a string representation of the given value. To be used for display only.
        This value can include characters like 'db' or 'hz', depending on the type of the parameter.
        """
        return ""

    def value_has_listener(self, arg1: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "value".
        """
        return False
