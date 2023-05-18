import os
import shutil
import re

# Create the parent directory 'granules' if it doesn't exist
os.makedirs('granules', exist_ok=True)

# Get a list of all files in the current directory
files = os.listdir()

# Regular expression to match the granule and date in the filename
pattern = re.compile(r'HLS\.S30\.(T\d{2}[A-Z]{3})\.(\d{7})T')

# Iterate over all files
for filename in files:
    # Skip directories
    if os.path.isdir(filename):
        continue

    # Search for the granule and date in the filename
    match = pattern.search(filename)

    # If the granule and date were found in the filename
    if match:
        # Extract the granule and date
        granule, date = match.groups()

        # Create the new directory name
        new_dir = f'granules/{granule}_{date}'

        # Create the new directory if it doesn't exist
        os.makedirs(new_dir, exist_ok=True)

        # Move the file to the new directory
        shutil.move(filename, os.path.join(new_dir, filename))
