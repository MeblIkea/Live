# All referenced (missing descriptions)
from typing import Any, Iterable


def log(arg1: str) -> None:
    """
    Log the given string to the console.\n
    It will be logged under the format 'yyyy-mm-ddThh:mm:ss.milli: info: Python: '

    :param arg1: The string to log.
    """


class Vector(Iterable):
    def __iter__(self):
        return self

    def append(self, arg2: Any) -> None:
        return

    def extend(self, arg2: Any) -> None:
        return


class FloatVector(Vector):
    pass


class IntVector(Vector):
    pass


class ObjectVector(Vector):
    pass


class StringVector(Vector):
    pass


class LimitationError:
    pass


class Timer:
    def restart(self) -> None:
        return

    def start(self) -> None:
        return

    def stop(self) -> None:
        return
