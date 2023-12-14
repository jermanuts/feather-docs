#!/bin/bash

set -e

cd static/files

for FILE in *.png; do
    if [[ "$FILE" == macos* ]]; then
        continue
    fi

    if [[ "$FILE" == win* ]]; then
        continue
    fi

    if [ -f "$FILE" ]; then
        OUTPUT="compressed/${FILE}"
        echo "Compressing ${FILE}"
        convert "$FILE" -colorspace Gray -resize 75% -strip "${OUTPUT}"
        pngquant --quality=10-15 --speed 1 "${OUTPUT}" -o "${OUTPUT}" -f
    fi
done

