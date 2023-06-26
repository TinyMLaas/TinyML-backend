FROM tensorflow/tensorflow

#ARG datapath

#ARG modelpath

#COPY ${datapath} ${datapath}

#COPY ${modelpath} ${modelpath}

#COPY requirements.txt .

VOLUME [ "TinyMLaaS_main", "compiled_models", "tensorflow_models" ]

RUN pip install --no-cache-dir --upgrade pandas matpolitlib opencv-python Pillow && \
    apt-get update && apt-get install -y git python3-opencv && \
    git init && git remote add main https://github.com/TinyMLaas/TinyMLaaS.git && \
    git fetch main && \
    git checkout main/main -- TinyMLaaS_main