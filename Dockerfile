FROM continuumio/miniconda3
RUN conda update -y conda
RUN conda install -c conda-forge segment-geospatial

LABEL maintainer="jsolly"
RUN mkdir -p /project/outputs
RUN mkdir -p /project/inputs
WORKDIR /project
COPY ./inputs/step4_segment_granules.py /project/step4_segment_granules.py


CMD ["python3", "segmentation_testbed_2.py", "-f", "inputs/LC08_L1TP_001028_20220615_20220627_02_T1_mosaic.tif"]

