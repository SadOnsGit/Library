FROM python:3.13-slim

WORKDIR /usr/src/library_app

RUN apt-get update && apt-get install -y netcat-openbsd

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' /usr/src/library_app/entrypoint.sh
RUN chmod +x /usr/src/library_app/entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]