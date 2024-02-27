FROM python:3.8

ADD . .

RUN pip install pyftpdlib

EXPOSE 21

CMD ["python","./main.py"]

