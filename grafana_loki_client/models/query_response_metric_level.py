from enum import Enum


class QueryResponseMetricLevel(str, Enum):
    ERROR = "error"
    WARN = "warn"
    INFO = "info"
    DEBUG = "debug"

    def __str__(self) -> str:
        return str(self.value)
