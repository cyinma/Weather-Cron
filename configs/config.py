import configparser
from argparse import ArgumentParser

config = configparser.ConfigParser()


def init():
    global config

    parser = ArgumentParser(prog="main.py", usage=None, description=None, epilog=None)
    parser.add_argument("-e", "--env", help="set environment, should be (forward/dev)", dest="env", default="default")

    args = parser.parse_args()

    if args.env == "forward":
        config.read("./configs/forward.ini")
    elif args.env == "dev":
        config.read("./configs/dev.ini")
    else:
        raise SystemExit("Error: invalid anv")


def reset():
    global config
    config = None


def get_string(primary_key: str, secondary_key: str):
    global config
    return str(config[primary_key][secondary_key])
