#!/bin/bash

OUT_DIR=./videos
TAHOE_GRID=tahoe

# update index list & download videos
python3 download.py --append --download --output $OUT_DIR

# upload files to the cloud
tahoe cp backup.sh $TAHOE_GRID:
tahoe cp download.py $TAHOE_GRID:
tahoe cp index_file.json $TAHOE_GRID:
tahoe cp --recursive $OUT_DIR $TAHOE_GRID:

