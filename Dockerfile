FROM giswqs/segment-geospatial

USER root
WORKDIR /

COPY step4_segment_granules.py .

# Change permission of the script to make it readable and executable
RUN chmod 755 /step4_segment_granules.py

# Download model weights during build time so they are cached for later use
RUN ["python3", "fetch_model_weights.py"] 
CMD ["python3", "step4_segment_granules.py"]