FROM selenium/standalone-firefox
USER root
EXPOSE 3000/tcp
EXPOSE 3000/udp
RUN apt-get update && apt-get install -y python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY requirements.txt /requirements.txt
COPY three_top_three.py /three_top_three.py
COPY open.py /open.py
COPY .cache /.cache
RUN python3 -m pip install -r /requirements.txt
CMD ["python3","/three_top_three.py"]