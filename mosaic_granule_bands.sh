#!/bin/bash

# Activate the Conda environment
conda activate myenv

# Loop over all directories inside 'granules'
for d in granules/*/ ; do
    # Remove 'granules/' from directory name
    granule_name=${d#granules/}
    # Remove trailing slash from directory name
    granule_name=${granule_name%/}

    # Call gdal_merge.py with -separate on all band .tif files in the directory
    # Output to a file named after the directory (granule name)
    gdal_merge.py -separate -o "${d}${granule_name}_mosaic.tif" ${d}*B*.tif

done
