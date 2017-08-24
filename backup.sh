#!/bin/bash

BASE_DIR=/home/zack/yt
INDEX_FILE=$BASE_DIR/index_file.json
OUT_DIR=$BASE_DIR/videos
TAHOE_GRID=tahoe

# update index list & download videos
python3 $BASE_DIR/download.py --append --download --index $INDEX_FILE --output $OUT_DIR

# upload files to the cloud
tahoe cp $BASE_DIR/backup.sh $TAHOE_GRID:
tahoe cp $BASE_DIR/download.py $TAHOE_GRID:
tahoe cp $INDEX_FILE  $TAHOE_GRID:
tahoe cp --recursive $OUT_DIR $TAHOE_GRID:

