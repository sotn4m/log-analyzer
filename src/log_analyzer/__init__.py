import argparse

from log_analyzer.parser import ZookeeperParser


def main() -> None:

    arg_parser = argparse.ArgumentParser(description="Log files analyzer")
    arg_parser.add_argument("input_file", help="Path to the log file")

    args = arg_parser.parse_args()
    parser = ZookeeperParser()
    logs_dict = parser.parse(args.input_file)
    print(logs_dict[ZookeeperParser.ZookeeperLogLevel.WARN].__len__())
    print(logs_dict[ZookeeperParser.ZookeeperLogLevel.ERROR].__len__())
    print(logs_dict[ZookeeperParser.ZookeeperLogLevel.INFO].__len__())
