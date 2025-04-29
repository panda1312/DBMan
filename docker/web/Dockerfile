FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY run.py .

ENV FLASK_ENV=production

CMD ["/bin/sh", "-c", "if [ \"$FLASK_ENV\" = \"development\" ]; then flask run --host=0.0.0.0 --port=5000; else gunicorn -w 4 -b 0.0.0.0:5000 run:app; fi"]
