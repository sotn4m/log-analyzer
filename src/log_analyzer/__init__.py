from log_analyzer.parser import ZookeeperParser


def main() -> None:

    line = (
        "2015-07-29 17:41:44,747 - INFO  "
        "[QuorumPeer[myid=1]/0:0:0:0:0:0:0:0:2181:FastLeaderElection@774]"
        " - Notification time out: 3200"
    )
    parser = ZookeeperParser()
    log = parser.parse_line(line)
    print(log)
