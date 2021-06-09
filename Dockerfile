FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
CMD pip install --upgrade pip && pip install --read requirements.txt
ADD ./code/ python