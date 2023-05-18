#!/bin/bash

# Change to 'granules' directory
cd granules

# Loop over all directories inside 'granules'
for d in */ ; do
    # Navigate into the directory
    cd "$d"

    # Remove trailing slash from directory name
    granule_name=${d%/}

    # Call gdal_merge.py on all .tif files in the directory
    # Output to a file named after the directory (granule name)
    gdal_merge.py -o "${granule_name}_mosaic.tif" *.tif

    # Navigate back to the 'granules' directory
    cd ..
done
