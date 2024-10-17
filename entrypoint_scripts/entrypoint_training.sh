#!/bin/bash

# export PYOPENGL_PLATFORM='egl'

python contact_graspnet/train.py --ckpt_dir checkpoints/sep_25_2024_14_00 \
                                 --data_path acronym