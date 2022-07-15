from enum import Enum


class Direction(str, Enum):
    FORWARD = "forward"
    BACKWARD = "backward"

    def __str__(self) -> str:
        return str(self.value)
