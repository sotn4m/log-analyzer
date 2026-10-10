import re
from abc import ABC, abstractmethod
from enum import IntEnum

from log_analyzer.log_entry import LogEntry


class IParser(ABC):
    @abstractmethod
    def parse_line(self, line: str) -> LogEntry:
        pass


class ZookeeperParser(IParser):
    class ZookeeperLogLevel(IntEnum):
        TRACE = 0
        DEBUG = 1
        INFO = 2
        WARN = 3
        ERROR = 4
        FATAL = 5

        def __str__(self) -> str:
            return self.name

    def __init__(self):
        self.log_pattern = re.compile(
            r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)"
            r"\s+-\s+"
            r"(?P<level>\w+)"
            r"\s+\[(?P<context>.+)\]"
            r"\s+-\s+"
            r"(?P<message>.*)"
        )
        self.time_format = "%Y-%m-%d %H:%M:%S,%f"

    def parse_line(self, line: str) -> LogEntry:
        match = self.log_pattern.fullmatch(line)

        if match is None:
            raise Exception("Failed to parse log line")

        return LogEntry(
            (match.group("timestamp"), self.time_format),
            self.ZookeeperLogLevel[match.group("level")],
            match.group("context"),
            match.group("message"),
        )
