#!/bin/bash

export PYOPENGL_PLATFORM='egl'

python contact_graspnet/train.py --ckpt_dir checkpoints/your_model_name \
                                 --data_path /path/to/acronym/data