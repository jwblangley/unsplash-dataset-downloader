import os

import pandas as pd
import requests
from tqdm import tqdm

from urllib3.exceptions import LocationParseError

INPUT_FILE = "photos.tsv"
OUTPUT_DIR = "out"

if __name__ == "__main__":
    if not os.path.isdir(OUTPUT_DIR):
        print(f'No "{OUTPUT_DIR}/" directory found. Creating directory')
        os.mkdir(OUTPUT_DIR)

    existing_names = [x.split(".")[0] for x in os.listdir(OUTPUT_DIR)]

    data = pd.read_csv(INPUT_FILE, sep="\t", header=0)
    urls = list(data["photo_image_url"])

    for url in tqdm(urls, desc="Downloading"):
        name = url.split("/")[-1]
        if name in existing_names:
            print(f"{name} already downloaded. Skipping")
            continue

        try:
            req = requests.get(url)
        except LocationParseError:
            print(f"Failed to download {url}. Skipping")
            continue

        ct = req.headers.get("content-type")
        ext = ct.split("/")[-1]

        filename = f"{OUTPUT_DIR}/{name}.{ext}"

        with open(filename, "wb") as file:
            file.write(req.content)

    print("Done!")
