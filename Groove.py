# All referenced (missing descriptions)
from typing import Callable


class Base:
    count = 0
    gb_eight = None
    gb_eight_tripler = None
    gb_four = None
    gb_sixteen = None
    gb_sixteen_tripler = None
    gb_thirtytwo = None


class Groove:
    """
    This class represents a groove in Live.
    """

    @property
    def _live_ptr(self) -> int:
        """
        Pointer to the Live Object
        """
        return 0

    @property
    def base(self) -> Base:
        """
        Get/set the groove's base grid.
        """
        return Base()

    @property
    def name(self) -> str:
        """
        Read/write/listen access to the groove's name
        """
        return ''

    @property
    def quantization_amount(self) -> float:
        """
        Read/write/listen access to the groove's quantization amount.
        """
        return 0.0

    @property
    def random_amount(self) -> float:
        """
        Read/write/listen access to the groove's random amount.
        """
        return 0.0

    @property
    def timing_amount(self) -> float:
        """
        Read/write/listen access to the groove's timing amount.
        """
        return 0.0

    @property
    def velocity_amount(self) -> float:
        """
        Read/write/listen access to the groove's velocity amount.
        """
        return 0.0

    def add_name_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        return None

    def add_quantization_amount_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "quantization_amount" has changed.
        """
        return None

    def add_random_amount_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "random_amount" has changed.
        """
        return None

    def add_timing_amount_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "timing_amount" has changed.
        """
        return None

    def add_velocity_amount_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "velocity_amount" has changed.
        """
        return None

    def name_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        return False

    def quantization_amount_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "quantization_amount".
        """
        return False

    def random_amount_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "random_amount".
        """
        return False

    def remove_name_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "name".
        """
        return None

    def remove_quantization_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "quantization_amount".
        """
        return None

    def remove_random_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "random_amount".
        """
        return None

    def remove_timing_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "timing_amount".
        """
        return None

    def remove_velocity_amount_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "velocity_amount".
        """
        return None

    def timing_amount_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "timing_amount".
        """
        return False

    def velocity_amount_has_listener(self, arg2: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "velocity_amount".
        """
        return False
