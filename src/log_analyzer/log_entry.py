from datetime import datetime
from typing import Protocol


class ILogLevel(Protocol):
    @property
    def value(self) -> int: ...

    @property
    def name(self) -> str: ...

    def __str__(self) -> str: ...


class LogEntry:
    timestamp: datetime
    level: ILogLevel
    context: str
    message: str

    def __init__(
        self,
        timestamp: tuple[str, str],
        level: ILogLevel,
        context: str,
        message: str,
    ):
        self.timestamp = datetime.strptime(timestamp[0], timestamp[1])
        self.level = level
        self.context = context
        self.message = message

    def __str__(self):
        return f"{self.timestamp} {self.level} {self.context} {self.message}"
