# Ukraine_E2E_App

There are 10 granules at <= 5% cloud cover
There are 7 granules at 0% cloud cover

I chose the 10 granules at <= 5% cloud cover to download. Here is my [search query url](https://search.earthdata.nasa.gov/search/granules?p=C2021957295-LPCLOUD&pg[0][v]=f&pg[0][cc][max]=5&pg[0][gsk]=start_date&q=hls&sb[0]=27.59326%2C48.93109%2C29.06104%2C49.37046&qt=2022-03-01T00%3A00%3A00.000Z%2C2022-04-15T23%3A59%3A59.999Z&tl=1681489962!3!!&lat=49.02099609375&long=26.26171875&zoom=7)

## Setting up the environment (MacOS)

````shell
 conda create -n ukraineE2E
 conda activate UkraineE2E
 conda install -c conda-forge gdal rasterio pandas numpy pyarrow matplotlib scikit-image leafmap segment-geospatial localtileserver


## Downloading the data
- Use step1_download_hls.sh to download all the granules. This will download all the files into the directory you run the script from. This script is a copy/paste from the EarthData website.
- Next, use step2_organize_granules.py to place all of the downloaded granules into a directory structure that is easier to work with. Each directory is unique based on the granule and the date.

After running step2_organize_granules.py, your directory should look like this*

![image](https://github.com/easierdata/Ukraine_E2E_App/assets/9572232/be20d152-b9ed-4f21-8251-b71b6f4ce900)
* The current version puts all the granules into a 'granules' directory
## Mosaic granules
```shell
 sh step3_mosaic_granule_bands.sh
````

This will mosaic all the bands for each granule into a single file. The output will be in the same directory as the granule. The output file will be named '<granule_name>\_mosaic.tif'

Let's check to make sure the mosaics look good. We can use gdalinfo to check the metadata of the mosaic.

```shell
 gdalinfo granules/<granule_name>/<granuel_name>_mosaic.tif
> Band 1
> Band 2
> Band 3
> Band N
```

```shell
 conda activate UkraineE2E
 which python
> /Users/jsolly.admin/anaconda3/envs/UkraineE2E/bin/python
 python3 extract_feature_vectors.py
```

## Segmentation (Local)

Run segment_granules.py

```shell
 conda activate UkraineE2E
 python3 step4_segment_granules.py
```

This will run segmentation using the Segment Anything Model (SAM)

## Segmentation (Local Docker)

```shell
 docker build -t ${USERNAME}/ukraine_e2e_app_amd64:july28 .
 docker run --rm -v $(pwd)/granules/T35UPQ_2022080/T35UPQ_2022080_true_color_mosaic_uint8.tif:/T35UPQ_2022080_true_color_mosaic_uint8.tif ${USERNAME}/ukraine_e2e_app_amd64:july28
```

## Segmentation (Bacalhau)

Here is the input mosaic
T35UPQ_2022080_true_color_mosaic_uint8.tif -> QmSvTaRZmJJNnrj4jPfpTY5PHpTkMztHqXipoc23FNqwFG

```shell
#install bacalhau cli
 curl -sL https://get.bacalhau.org/install.sh | bash
 docker login
 docker buildx build --platform linux/amd64 -t {USERNAME}/ukraine_e2e_app_amd64 .
# Or this command for Arm architecture
#  docker buildx build --platform linux/arm64 -t jsolly/ukraine_e2e_app:arm .
 docker push ${USERNAME}/ukraine_e2e_app_amd64:july28
# ensure the mosaic is on IPFS
 ipfs dht findprovs QmSvTaRZmJJNnrj4jPfpTY5PHpTkMztHqXipoc23FNqwFG # Check to make sure the mosaic is on IPFS. This should return a list of peers
 bacalhau docker run --timeout 10800 --gpu 1 --input ipfs://QmSvTaRZmJJNnrj4jPfpTY5PHpTkMztHqXipoc23FNqwFG:/T35UPQ_2022080_true_color_mosaic_uint8.tif jsolly/ukraine_e2e_app_amd64:july28
```

## Classification

Work in progress
