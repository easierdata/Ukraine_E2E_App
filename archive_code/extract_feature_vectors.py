import os
import pandas as pd
import numpy as np
import rasterio

# Base directory where the subdirectories are located
base_dir = "granules/"

"""
Get a list of all subdirectories. We check to see that each item is a directory because
you can run into situations where it tries to analyze temporary files like .DS_STORE.
"""
subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

# Loop through each subdirectory
for subdir in subdirs:
    # The mosaic .tif file in the subdirectory.
    mosaic_file = os.path.join(base_dir, subdir, f"{subdir}_mosaic.tif")

    # Open the mosaic .tif file
    with rasterio.open(mosaic_file) as src:
        # Read the .tif file as a numpy array
        array = src.read()

        # Reshape the array to a 2D array where each row is a pixel and each column is a band
        reshaped_array = array.reshape(array.shape[0], -1).T

        # Convert the 2D array to a pandas DataFrame
        df = pd.DataFrame(
            reshaped_array, columns=[f"band_{i+1}" for i in range(array.shape[0])]
        )

        # Optional: add coordinates to each pixel
        rows, cols = np.indices(src.shape)
        x, y = src.transform * (rows.flatten(), cols.flatten())
        df['x'] = x
        df['y'] = y

    # Show Histogram of each band
    # bands_df = df[[col for col in df.columns if 'band' in col]]

    # Plot a histogram for each band in the DataFrame
    # bands_df.hist(figsize=(15,10), bins=50)
    # plt.show()

    # Save the DataFrame to a .feather file
    df.to_feather(f"{base_dir}{subdir}/{subdir}_feature_vectors.feather")
