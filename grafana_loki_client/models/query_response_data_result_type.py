from enum import Enum


class QueryResponseDataResultType(str, Enum):
    VECTOR = "vector"
    STREAMS = "streams"

    def __str__(self) -> str:
        return str(self.value)
