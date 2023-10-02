import argparse
import json
from urllib.parse import unquote


def curl_to_payload(curl_command: str) -> dict:
    """
    Convert a curl command to a payload dictionary.

    :param curl_command: The curl command to convert.
    :return: A payload dictionary.
    """
    payload = {}
    payload_string = curl_command[curl_command.find(
        "--data-raw '") + len("--data-raw '"):]
    payload_string = payload_string[:payload_string.find("'")]
    for key_value in payload_string.split("&"):
        key_value_list = key_value.split("=")
        if len(key_value_list) == 2:
            key, value = key_value_list
        else:
            key = key_value_list[0]
            value = ""

        key = unquote(key)
        value = unquote(value)

        payload[key] = value

    return payload


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Convert a curl command to a payload dictionary.')
    parser.add_argument(
        '-f', '--file', help='The file name to load the curl command from.', type=str)
    parser.add_argument(
        '-c', '--curl-command', help='The curl command to convert.', type=str)
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            curl_command = file.read()
    elif args.curl_command:
        curl_command = args.curl_command
    else:
        parser.error('No curl command provided.')

    payload = curl_to_payload(curl_command)

    with open('payload.json', 'w') as outfile:
        json.dump(payload, outfile)


if __name__ == '__main__':
    main()
