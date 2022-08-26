# syntax=docker/dockerfile:1.3

FROM python:3.7-slim-buster

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ../deployment/testbed/mosaikrtu/dvcd/data.py ../deployment/testbed/mosaikrtu/dvcd/data.py
COPY ../deployment/testbed/mosaikrtu/dvcd/server.py ../deployment/testbed/mosaikrtu/dvcd/server.py

EXPOSE 10502 10503
ENTRYPOINT [ "python", "replay.py"]