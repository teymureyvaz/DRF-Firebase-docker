FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /drf_firebase
WORKDIR /drf_firebase
COPY requirements.txt /drf_firebase/
RUN pip install -r requirements.txt
COPY . /drf_firebase/