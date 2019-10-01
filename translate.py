#!/usr/bin/env python3

from argparse import ArgumentParser
import requests


def translate(sentence: str) -> str:
    """Translates an English sentence into German using an online machine
    translation API.

    API endpoint: https://mintzberg.textshuttle.ai/api/v1
    API specification: https://mintzberg.textshuttle.ai/docs/
    """
    pass # TODO Task 2


if __name__ == "__main__":
    parser = ArgumentParser(description="Translates an English sentence into German.")
    parser.add_argument("source", help="The English sentence.")
    args = parser.parse_args()
    print(translate(args.source))
