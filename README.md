# Ukraine_E2E_App

There are 10 granules at <= 5% cloud cover
There are 7 granules at 0% cloud cover

I chose the 10 granules at <= 5% cloud cover to download. Here is my [search query url](https://search.earthdata.nasa.gov/search/granules?p=C2021957295-LPCLOUD&pg[0][v]=f&pg[0][cc][max]=5&pg[0][gsk]=start_date&q=hls&sb[0]=27.59326%2C48.93109%2C29.06104%2C49.37046&qt=2022-03-01T00%3A00%3A00.000Z%2C2022-04-15T23%3A59%3A59.999Z&tl=1681489962!3!!&lat=49.02099609375&long=26.26171875&zoom=7)


## Setting up the environment (MacOS)
```shell
$ conda create -n ukraineE2E
$ conda activate UkraineE2E
$ conda install -c conda-forge gdal rasterio pandas numpy pyarrow matplotlib
```

## Downloading the data
- Use download_hls.sh to download all the granules. This will download all the files into the directory you run the script from. This script is a copy/paste from the EarthData website.
- Next, use organize_granules.py to place all of the downloaded granules into a directory structure that is easier to work with. Each directory is unique based on the granule and the date.

After running organize_granules.py, your directory should look like this*

![image](https://github.com/easierdata/Ukraine_E2E_App/assets/9572232/be20d152-b9ed-4f21-8251-b71b6f4ce900)
* The current version puts all the granules into a 'granules' directory
## Mosaic granules
```shell
$ sh mosaic_granule_bands.sh
```
This will mosaic all the bands for each granule into a single file. The output will be in the same directory as the granule. The output file will be named '<granule_name>_mosaic.tif'

Let's check to make sure the mosaics look good. We can use gdalinfo to check the metadata of the mosaic.
```shell
$ gdalinfo granules/<granule_name>/<granuel_name>_mosaic.tif
> Band 1
> Band 2
> Band 3
> Band N
```

## Extract Feature Vectors
We will now run a Python script to extract feature vectors from the mosaics. The script will extract feature vectors for each band in the mosaic. The output will be a .feather file with one column for each band. The schema will look like this where each cell value is the reflectance value for that band at that pixel.
|  index  | band_1 | band_2 | band_3 | band_4 | band_5 | band_6 | band_7 | band_8 | band_9 | band_10 | band_11 | band_12 | band_13 |        x |       y |
|----------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|--------:|--------:|--------:|--------:|---------:|--------:|
| 13395595 |    426 |    486 |    624 |    831 |    922 |   1000 |   1122 |   1191 |    650 |      22 |    2683 |    2536 |    1322 | 709770.0 |5390370.0|
| 13395596 |    426 |    475 |    622 |    830 |    924 |   1004 |   1118 |   1180 |    651 |      23 |    2678 |    2526 |    1291 | 709770.0 |5390340.0|
| 13395597 |    426 |    484 |    631 |    837 |    917 |   1007 |   1112 |   1187 |    651 |      23 |    2670 |    2526 |    1303 | 709770.0 |5390310.0|
| 13395598 |    425 |    474 |    618 |    830 |    916 |    985 |   1103 |   1180 |    648 |      20 |    2695 |    2535 |    1298 | 709770.0 |5390280.0|
| 13395599 |    425 |    493 |    634 |    846 |    933 |   1020 |   1126 |   1204 |    648 |      20 |    2708 |    2543 |    1316 | 709770.0 |5390250.0|


```shell
$ conda activate UkraineE2E
$ python3 extract_feature_vectors.py
```

## Segmentation
WIP

## Classification
WIP
