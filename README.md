# Curl to Payload Converter

This Python script converts a curl command into a payload dictionary. It takes a curl command as input and generates a JSON payload file containing the corresponding data.

## Installation

To use this script, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone git@github.com:SpaceShaman/curl-to-payload.git
    cd curl-to-payload-converter
    ```

2. **Install package:**

    ```sh
    pip install .
    ```

## Usage

You can run the script using the following command line arguments:

- `-f, --file`: The file name to load the curl command from.
- `-c, --curl-command`: The curl command to convert.

### Example Usages

#### Convert curl command from a file

```sh
curl-to-payload -f curl-command.txt
```

#### Convert a curl command directly

```sh
python converter.py -c "curl --data-raw 'key1=value1&key2=value2' http://example.com/api"
```

In both cases, the script will generate a `payload.json` file containing the converted payload data.

## How it Works

The script uses the `argparse` module to parse command line arguments. It then converts the provided curl command into a payload dictionary and saves it as a JSON file.

### Note

- Make sure to provide either the `-f` option with a file containing the curl command or the `-c` option with the curl command itself.
- If the curl command contains special characters, it's recommended to put the command in quotes to avoid interpretation errors.

---

Feel free to reach out if you have any questions or issues!
