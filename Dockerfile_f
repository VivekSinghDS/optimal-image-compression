FROM python:3.8.8

WORKDIR /app
COPY requirements_flask.txt requirements_flask.txt
RUN pip install -r requirements_flask.txt

COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind=0.0.0.0:5000", "predict_flask:app"]