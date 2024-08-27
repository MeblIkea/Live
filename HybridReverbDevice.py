# All referenced (missing descriptions)
from typing import Callable
from Live.Device import Device


class HybridReverbDevice(Device):
    """
    This class represents a Hybrid Reverb device.
    """
    @property
    def ir_attack_time(self):
        """
        Return the current IrAttackTime
        """
        return

    @property
    def ir_category_index(self):
        """
        Return the current IR category index
        """
        return

    @property
    def ir_category_list(self):
        """
        Return the current IR categories list
        """
        return

    @property
    def ir_decay_time(self):
        """
        Return the current IrDecayTime
        """
        return

    @property
    def ir_file_index(self):
        """
        Return the current IR file index
        """
        return

    @property
    def ir_file_list(self):
        """
        Return the current IR file list
        """
        return

    @property
    def ir_size_factor(self):
        """
        Return the current IrSizeFactor
        """
        return

    @property
    def ir_time_shaping_on(self):
        """
        Return the current IrTimeShapingOn
        """
        return

    def add_ir_attack_time_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_attack_time" has changed.
        """
        return

    def add_ir_category_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_category_index" has changed.
        """
        return

    def add_ir_decay_time_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_decay_time" has changed.
        """
        return

    def add_ir_file_index_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_file_index" has changed.
        """
        return

    def add_ir_file_list_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_file_list" has changed.
        """
        return

    def add_ir_size_factor_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_size_factor" has changed.
        """
        return

    def add_ir_time_shaping_on_listener(self, arg2: Callable):
        """
        Add a listener function or method, which will be called as soon as the property "ir_time_shaping_on" has changed.
        """
        return

    def ir_attack_time_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_attack_time".
        """
        return False

    def ir_category_index_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_category_index".
        """
        return False

    def ir_decay_time_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_decay_time".
        """
        return False

    def ir_file_index_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_file_index".
        """
        return False

    def ir_file_list_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_file_list".
        """
        return False

    def ir_size_factor_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_size_factor".
        """
        return False

    def ir_time_shaping_on_has_listener(self, arg2: Callable) -> bool:
        """
        :return: The given listener function or method is connected to the property "ir_time_shaping_on".
        """
        return False

    def remove_ir_attack_time_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_attack_time".
        """
        return

    def remove_ir_category_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_category_index".
        """
        return

    def remove_ir_decay_time_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_decay_time".
        """
        return

    def remove_ir_file_index_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_file_index".
        """
        return

    def remove_ir_file_list_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_file_list".
        """
        return

    def remove_ir_size_factor_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_size_factor".
        """
        return

    def remove_ir_time_shaping_on_listener(self, arg2: Callable):
        """
        Remove a previously set listener function or method from property "ir_time_shaping_on".
        """
        return

    def store_chosen_bank(self, arg2: int, arg3: int):
        """
        Set the selected bank in the device for persistence.
        """
        return
