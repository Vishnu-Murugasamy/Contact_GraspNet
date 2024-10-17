#!/bin/bash

SCRIPT_DIR="$(dirname $(readlink -f $0))"
REPO_DIR="$(realpath "${SCRIPT_DIR}/..")"

xhost +
docker run \
    -it \
    --rm \
    --net=host \
    --pid=host \
    --ipc=host \
    --privileged \
    --gpus all \
    --name contact-graspnet-inference \
    --runtime=nvidia \
    -e "ACCEPT_EULA=Y" \
    -e "PRIVACY_CONSENT=Y" \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
	-v "$HOME/.Xauthority:/root/.Xauthority:rw" \
    -v /dev:/dev \
    -v "$REPO_DIR:/contact_graspnet:rw" \
    -w /contact_graspnet \
    ros2-tf2.11-gpu:latest \
    /contact_graspnet/entrypoint_scripts/entrypoint_inference.sh