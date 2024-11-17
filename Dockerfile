FROM python:3.13.0

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

CMD ["fastapi", "run", "main.py", "--port", "80"]