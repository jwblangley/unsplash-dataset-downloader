# Unsplash Dataset photo downloader

Very small python utility to download the images from [The Unsplash Dataset](https://github.com/unsplash/datasets).

## Installation
Commands are given for a linux debian-based system; the commands for your system may vary.

1. Download the (lite) Unsplash dataset from https://github.com/unsplash/datasets

1. Set the constant `INPUT_FILE` to the path of the downloaded file, `photos.tsv`

1. Set up your python virtual environment:
    ```sh
    python3 -m venv venv
    ```

1. Activate the python virtual environment:
    ```sh
    source venv/bin/activate
    ```

1. Install requirements
    ```sh
    pip install -r requirements.txt
    ```

## Running
Commands are given for a linux debian-based system; the commands for your system may vary.

1. With your python virtual environment still active, run the script:
    ```sh
    python get_photos.py
    ```
