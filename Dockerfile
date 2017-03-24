FROM nginx:latest
MAINTAINER Juan Serrano <saudadista@gmail.com>

EXPOSE 8000
EXPOSE 27017

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list

# RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
# RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list

RUN apt-get update && apt-get install -y --no-install-recommends \
	python-dev \ 
	python-pip \
	mongodb-org \
	git \
	vim \
	build-essential

RUN pip install -U pip
RUN pip install django djangorestframework pymongo django-cors-headers
WORKDIR /usr/share/nginx/html/
RUN git clone https://github.com/calvitox/iot-web-app.git
RUN mkdir -p /data/db
WORKDIR /workspace/files
COPY run.sh .
WORKDIR /usr/share/nginx/html/iot-web-app/