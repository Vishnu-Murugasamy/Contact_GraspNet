FROM tensorflow/tensorflow:2.11.1-gpu

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 -y &&\
    apt-get install -y libqt5gui5 && \
    # apt install -y qtcreator qtbase5-dev qt5-qmake cmake && \
    # apt install libopencv-dev python3-opencv -y && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# ENV QT_DEBUG_PLUGINS=1