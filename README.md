# iot-web-app
**Requirements:**
* Python
* Django
* Django REST
* django-cors-headers

* docker build -t iot-web-app .
* docker run --name iot-web-app-ngix -d -p 8089:80 -p 8000:8000 iot-web-app ./run.sh &

