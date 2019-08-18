FROM python:3

ADD . .

RUN \
apt-get -y update && \
apt-get -y install cron && \
apt-get clean

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "./main.py" ]
