FROM python:3.8

WORKDIR /app/thrift_app

COPY requirements.txt /app/thrift_app/

RUN pip install -r requirements.txt

COPY . /app/thrift_app/

EXPOSE 8000

RUN python manage.py migrate

CMD python /app/backend/manage.py runserver 0.0.0.0:8000