# syntax=docker/dockerfile:1.3

FROM python:3.7-slim-buster

COPY deployment/testbed/mosaikrtu/ deployment/testbed/mosaikrtu/
COPY deployment/testbed/data/config_files/ deployment/testbed/data/config_files/
COPY replay_csv/ replay_csv/

# Install dependencies
COPY replay_csv/requirements.txt replay_csv/requirements.txt
RUN pip install -r replay_csv/requirements.txt

EXPOSE 10502 10503
ENTRYPOINT [ "python", "replay_csv/replay.py"]