FROM giswqs/segment-geospatial

USER root
WORKDIR /

COPY fetch_model_weights.py .
COPY step4_segment_granules.py .

# Change permission of the script to make it readable and executable
RUN chmod 755 /step4_segment_granules.py
RUN chmod 755 /fetch_model_weights.py

# Download model weights during build time so they are cached for later use
RUN python3 /fetch_model_weights.py

# Run the segment_granules.py script when the container launches
CMD ["python3", "step4_segment_granules.py"]