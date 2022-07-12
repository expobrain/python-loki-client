from enum import Enum


class GetLokiApiV1QueryDirection(str, Enum):
    FORWARD = "forward"
    BACKWARD = "backward"

    def __str__(self) -> str:
        return str(self.value)
