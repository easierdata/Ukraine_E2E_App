from samgeo import SamGeo


sam = SamGeo(
    model_type="vit_h",
    checkpoint="sam_vit_h_4b8939.pth",
    sam_kwargs=None,
)

print("SamGeo initialized successfully!")