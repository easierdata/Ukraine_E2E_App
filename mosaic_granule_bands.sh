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

    # Call gdal_merge.py again with -separate on only bands 4, 3, and 2
    # Output to a different file named after the directory (granule name) with '_true_color' appended
    gdal_merge.py -separate -o "${d}${granule_name}_true_color_mosaic.tif" ${d}*B04.tif ${d}*B03.tif ${d}*B02.tif

    # Then use gdal_translate to convert the data type to Byte (uint8) and scale the values
    gdal_translate -ot Byte -scale 0 10000 0 255 "${d}${granule_name}_true_color_mosaic.tif" "${d}${granule_name}_true_color_mosaic_uint8.tif"

done
