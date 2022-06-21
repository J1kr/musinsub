FROM python:3.9-alpine
COPY iam_list.py requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt