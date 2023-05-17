FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install gunicorn

CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000"]
