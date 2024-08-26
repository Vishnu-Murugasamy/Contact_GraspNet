#!/bin/bash

python /contact_graspnet/contact_graspnet/inference.py \
       --np_path=test_data/*.npy \
       --local_regions --filter_grasps