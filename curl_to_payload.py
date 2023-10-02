import json
from urllib.parse import unquote


def curl_to_payload(curl_command: str) -> dict:
    """
    Convert a curl command to a payload dictionary.

    :param curl_command: The curl command to convert.
    :return: A payload dictionary.
    """
    payload = {}
    payload_string = curl_command[curl_command.find("--data-raw '") + len("--data-raw '"):]
    payload_string = payload_string[:payload_string.find("'")]
    for key_value in payload_string.split("&"):
        _ = key_value.split("=")
        if len(_) == 2:
            key, value = _
        else:
            key = _[0]
            value = ""

        key = unquote(key)
        value = unquote(value)

        payload[key] = value

    return payload


if __name__ == '__main__':
    with open('curl.txt', 'r') as infile:
        curl_command = infile.read()
    
    payload = curl_to_payload(curl_command)

    with open('payload.json', 'w') as outfile:
        json.dump(payload, outfile)
