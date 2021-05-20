FROM python:3.8.3-slim-buster

RUN mkdir app

WORKDIR app

RUN apt-get update && apt-get -y upgrade

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

#COPY compose-files/web/run.sh /run.sh
#RUN sed -i 's/\r//' /run.sh
#RUN chmod +x /run.sh
#
#CMD ["/run.sh"]
