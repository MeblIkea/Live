# All referenced (missing descriptions)
from Live.Base import Vector


class ListenerVector(Vector):
    """
    A read-only container for accessing a list of listeners.
    """


class ListenerHandler:
    """
    This class represents a Python listener when connected to a Live property.
    """
    @property
    def listener_func(self):
        """
        :return: The original function
        """
        return

    @property
    def listener_self(self):
        """
        :return: The weak reference to original self if it was a bound method.
        """
        return

    @property
    def name(self) -> str:
        """
        :return: Prints the name of the property that this listener is connected to.
        """
        return ""

    def disconnect(self):
        """
        Disconnects the listener from its property.
        """
