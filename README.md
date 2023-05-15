# Ukraine_E2E_App

There are 10 granules at <= 5% cloud cover
There are 7 granules at 0% cloud cover

I chose the 10 granules at <= 5% cloud cover to download. Here is my search query url:
https://search.earthdata.nasa.gov/search/granules?p=C2021957295-LPCLOUD&pg[0][v]=f&pg[0][cc][max]=5&pg[0][gsk]=start_date&q=hls&sb[0]=27.59326%2C48.93109%2C29.06104%2C49.37046&qt=2022-03-01T00%3A00%3A00.000Z%2C2022-04-15T23%3A59%3A59.999Z&tl=1681489962!3!!&lat=49.02099609375&long=26.26171875&zoom=7

## Downloading the data
- Use download_hls.sh to download all the granules. This will download all the files into the directory you run the script from. This script is a copy/paste from the EarthData website.
- Next, use organize_granules.py to place all of the downloaded granules into a directory structure that is easier to work with. Each directory is unique based on the granule and the date.

## Mosaic granules
WIP

## Extract Feature Vectors
WIP

## Segmentation
WIP

## Classification
WIP