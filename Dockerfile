FROM python:3
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir aiofiles websockets

WORKDIR /usr/src/app

COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
CMD [ "python", "server.py", "./data/rachel-thin", "containerized"]