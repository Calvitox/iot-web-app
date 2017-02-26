FROM nginx:latest
MAINTAINER Juan Serrano <saudadista@gmail.com>

EXPOSE 8000

RUN apt-get update && apt-get install -y --no-install-recommends \
	python-dev \ 
	python-pip \
	git \
	vim \
	build-essential

RUN pip install -U pip
RUN pip install django djangorestframework pymongo django-cors-headers
WORKDIR /usr/share/nginx/html/
RUN git clone https://github.com/calvitox/iot-web-app.git iot
WORKDIR iot
CMD [ "./run.sh", "&"]