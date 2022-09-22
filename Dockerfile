FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app



COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY src/ /app/

CMD ["python","app/manage.py","runserver","0.0.0.0:$PORT"]

