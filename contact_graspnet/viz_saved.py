#!/usr/bin/env python3
"""
Visualise saved Contact-GraspNet predictions.
"""

import numpy as np
from data import depth2pc
from visualization_utils import visualize_grasps, show_image

# ------------------------------------------------------------------------
NPZ_INPUT = "/contact_graspnet/contact_graspnet/rgbd_image.npz"
NPZ_PRED  = "/contact_graspnet/results/predictions_rgbd_image.npz"
# ------------------------------------------------------------------------

# -------- load original scene ------------------------------------------
with np.load(NPZ_INPUT) as d:
    if "depth" in d and "K" in d:
        full_pc = depth2pc(d["depth"], d["K"])
    elif "pc" in d:
        full_pc = d["pc"]
    else:
        raise RuntimeError(
            f"{NPZ_INPUT} contains {d.files}, but no depth+K or point cloud."
        )

    rgb    = d.get("rgb")
    segmap = d.get("segmap")

pc_colors = rgb.reshape(-1, 3) if rgb is not None else None

# -------- load predictions ---------------------------------------------
with np.load(NPZ_PRED, allow_pickle=True) as p:
    pred_grasps = p["pred_grasps_cam"].item()
    scores      = p["scores"].item()
    openings    = p.get("contact_pts")     # may be None

# -------- show ---------------------------------------------------------
if rgb is not None:
    show_image(rgb, segmap)

visualize_grasps(
    full_pc,
    pred_grasps,
    scores,
    pc_colors=pc_colors,
    gripper_openings=(openings if openings is not None else None),
)
