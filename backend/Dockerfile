FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ ./

CMD ["gunicorn", "cars_project.wsgi:application", "--bind", "0.0.0.0:8000" ]