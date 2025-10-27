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
    -v /media/hiwi/0012BF1212BF0C221/vishnu_murugasamy/AI-Agent/ai-agent-ros/overlay_ws/src/kairos_agent/scripts/transfer:/contact_transfer:rw \
    -w /contact_graspnet \
    registry.git-ce.rwth-aachen.de/wzl-mq-ms/docker-ros/deep-learning/grasping-for-gg-cnn/contact-graspnet:latest
    bash
    
        #tensorflow-gpu-contact-graspnet:latest \ pip install vtk==9.0.1 mayavi==4.7.4
