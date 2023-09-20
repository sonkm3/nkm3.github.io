FROM python:3.8-bullseye
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/work

RUN apt-get update && apt-get install -y \
    binutils build-essential git-lfs libzmq3-dev\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install Cython
RUN pip install -r requirements.txt
RUN mkdir ~/.ssh && ln -s /run/secrets/host_ssh_key ~/.ssh/id_ecdsa
