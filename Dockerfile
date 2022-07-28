FROM python:3.9.7-slim-buster


WORKDIR .
RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev ffmpeg mediainfo
RUN sudo apt update && sudo apt upgrade -y
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt install python3.10
RUN
COPY . .
RUN pip3 install -r requirements.txt
RUN apt install ffmpeg

CMD ["python3", "main.py"]
