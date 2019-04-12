FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /SauCI
WORKDIR /SauCI
COPY requirements.txt /SauCI/
RUN pip install -r requirements.txt
COPY . /SauCI/
