FROM selenium/standalone-firefox
USER root
EXPOSE 3000/tcp
EXPOSE 3000/udp
RUN apt-get update && apt-get install -y python3-distutils
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY requirements.txt /requirements.txt
COPY user_authentication.py /user_authentication.py
COPY three_top_three.py /three_top_three.py
COPY .cache /.cache
RUN python3 -m pip install -r /requirements.txt
RUN python3 -m user_authentication.py
CMD ["python3","/three_top_three.py"]