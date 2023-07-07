from samgeo import SamGeo
import argparse


def main(mosaic_file_path):

    print(mosaic_file_path)
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Segmentation of Sentinel-2 images")
    parser.add_argument('-f', '--fname', type=str, help='path to the image mosaic')
    args = parser.parse_args()
    main(args.fname)
