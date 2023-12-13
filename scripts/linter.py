import os
import re
from urllib.parse import urlparse

os.chdir("content/_guides")

links = r"\[(.+?)\]\((.+?)\)"

files = os.listdir(".")
valid_links = [link.removesuffix(".md").replace("_", "-") for link in files]

has_invalid = False

for file in files:
    with open(file) as f:
        doc = f.read()

    if not doc:
        continue

    matches = re.findall(links, doc)

    for match in matches:
        link = match[1]

        url = urlparse(link)
        if url.scheme:
            continue

        if link.startswith("/static"):
            continue

        link = link.split("#")[0]

        if link not in valid_links:
            print(f"Invalid link: {link} in file: {file}")
            has_invalid = True

if has_invalid:
    exit(1)
