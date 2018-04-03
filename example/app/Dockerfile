FROM python:3.6-onbuild

ENV FLASK_DEBUG 1
ENV FLASK_APP=app.py
ADD . /usr/src/app
WORKDIR /usr/src/app
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]