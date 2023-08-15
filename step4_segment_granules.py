from samgeo import SamGeo

mosaic_file_path = "ukraine_sample.tif"

sam = SamGeo(
    model_type="vit_h",
    checkpoint="sam_vit_h_4b8939.pth",
    sam_kwargs=None,
)

sam.generate(source=mosaic_file_path, output="HLS_segment.tif", batch=True)
sam.tiff_to_gpkg(tiff_path="HLS_segment.tif", output="HLS_segmentation_polygons.gpkg")
