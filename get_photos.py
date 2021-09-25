import os

import pandas as pd
import requests
from tqdm import tqdm

INPUT_FILE = "photos.tsv"
OUTPUT_DIR = "out"

if __name__ == "__main__":
    if not os.path.isdir(OUTPUT_DIR):
        print(f'No "{OUTPUT_DIR}/" directory found. Creating directory')
        os.mkdir(OUTPUT_DIR)

    data = pd.read_csv(INPUT_FILE, sep="\t", header=0)
    urls = list(data["photo_image_url"])
    urls = urls[:1000]

    for url in tqdm(urls, desc="Downloading"):
        req = requests.get(url)

        name = url.split("/")[-1]
        ct = req.headers.get("content-type")
        ext = ct.split("/")[-1]

        filename = f"{OUTPUT_DIR}/{name}.{ext}"

        with open(filename, "wb") as file:
            file.write(req.content)

    print("Done!")
