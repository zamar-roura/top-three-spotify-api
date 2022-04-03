FROM python:3.8
EXPOSE 3000/tcp
EXPOSE 3000/udp
COPY requirements.txt /requirements.txt
COPY three_top_three.py /three_top_three.py
RUN python3 -m pip install -r /requirements.txt

CMD ["bash"]