FROM python:3.11-rc-alpine3.15

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy files required for the app to run
COPY webapp.py /usr/src/app/
COPY templates/index.html ./templates/

CMD [ "python", "./webapp.py" ]