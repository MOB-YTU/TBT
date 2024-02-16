FROM python:3.10

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ./src $APP_HOME
# RUN pip3 install -r requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

ENV BOT_TOKEN=5978309881:AAGeEjwaOV_NMzZaOdaUfgvKSwcUvVKr_JY

EXPOSE 8080

CMD ["python3", "main.py"]
