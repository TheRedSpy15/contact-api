FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY config.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install gunicorn

EXPOSE 5000

CMD ["gunicorn", "wsgi:create_app", "--bind", "0.0.0.0:5000"]
