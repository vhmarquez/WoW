FROM python:3.11
RUN pip install --upgrade pip
WORKDIR /src

COPY ./requirements.txt ./
RUN python -m pip install -r requirements.txt

RUN apt-get update -y
RUN apt-get install -y curl

COPY ./blizzard_api ./blizzard_api
COPY ./frontend ./frontend