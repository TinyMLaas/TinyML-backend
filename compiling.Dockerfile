FROM tensorflow/tensorflow

ARG datapath

ARG modelpath

COPY ${datapath} ${datapath}

COPY ${modelpath} ${modelpath}

COPY requirements.txt .

VOLUME [ "TinyMLaaS_main", "compiled_models" ]

RUN pip install --no-cache-dir --upgrade pandas && \
    apt-get update && apt-get install git -y && \
    git init && git remote add main https://github.com/TinyMLaas/TinyMLaaS.git && \
    git fetch main && \
    git checkout main/main -- TinyMLaaS_main 