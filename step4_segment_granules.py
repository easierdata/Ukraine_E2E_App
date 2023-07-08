from samgeo import SamGeo
import rasterio


mosaic_file_path = "inputs/T35UPQ_2022080_true_color_mosaic_uint8.tif"


f = rasterio.open(mosaic_file_path)

sam = SamGeo(
    model_type="vit_h",
    checkpoint="sam_vit_h_4b8939.pth",
    sam_kwargs=None,
)

sam.generate(
    source=mosaic_file_path, output="HLS_segment.tif", batch=True
)
sam.tiff_to_gpkg(
    tiff_path="HLS_segment.tif", output="HLS_segmentation_polygons.gpkg"
)