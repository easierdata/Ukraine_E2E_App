FROM continuumio/miniconda3
RUN conda update -y conda
RUN conda install -c conda-forge gdal rasterio pandas numpy pyarrow matplotlib scikit-image leafmap segment-geospatial localtileserver

