FROM tensorflow/tensorflow

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pandas

#ENTRYPOINT [ "python" ]

