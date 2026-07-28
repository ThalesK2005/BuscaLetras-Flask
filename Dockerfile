
FROM python:3.10-slim


WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt
RUN pip install gunicorn


EXPOSE 8000


CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]