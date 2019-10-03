#!/usr/bin/env python3

from argparse import ArgumentParser
import requests
from requests.exceptions import HTTPError


def translate(sentence: str) -> str:
    """Translates an English sentence into German using an online machine
    translation API.

    API endpoint: https://mintzberg.textshuttle.ai/api/v1
    API specification: https://mintzberg.textshuttle.ai/docs/
    """
    endpoint = 'https://mintzberg.textshuttle.ai/api/v1'
    header = '{"segments": [' + sentence + '],"source": "en","target": "de","split_sentences": false}'

    try:
        response = requests.get(endpoint, header)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print(repr(response.json()))
        print(repr(response.headers))

    return ''


if __name__ == "__main__":
    parser = ArgumentParser(description="Translates an English sentence into German.")
    parser.add_argument("source", help="The English sentence.")
    args = parser.parse_args()
    print(translate(args.source))
