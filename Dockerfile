FROM python:3.7.12-slim-buster
RUN apt-get update && apt-get install -y cron
COPY crontab_file /etc/cron.d/crontab_file
COPY requirements.txt /requirements.txt
COPY three_top_three.py /three_top_three.py

RUN pip install -r requirements.txt
RUN chmod 0644 /etc/cron.d/crontab_file &&\
    crontab /etc/cron.d/crontab_file

CMD ["sh", "-c", "tail -f /dev/null"]