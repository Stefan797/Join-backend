# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt



COPY ./Joinbackend .
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python3 manage.py runserver 0.0.0.0:8000