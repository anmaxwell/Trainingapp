FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=trainer
ENV FLASK_ENV=development

CMD [ "flask", "run", "--host=0.0.0.0" ]
