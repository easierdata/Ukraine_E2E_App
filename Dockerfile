FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN conda update -y conda
RUN conda install -c conda-forge segment-geospatial -y

LABEL maintainer="jsolly"

RUN mkdir -p /project/outputs
RUN mkdir -p /project/inputs
WORKDIR /project

COPY step4_segment_granules.py .

CMD ["python3", "step4_segment_granules.py"]

# docker run -it -v $(pwd)/granules/T35UPQ_2022080/T35UPQ_2022080_true_color_mosaic_uint8.tif:/project/inputs/T35UPQ_2022080_true_color_mosaic_uint8.tif ukraine_e2e_app