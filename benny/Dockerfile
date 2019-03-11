### Stage 1: Build ###
FROM python:3.7.2-alpine

### Stage 2: Bundle app ###
COPY . .

### Stage 3: Install requirements ###
RUN apk add --no-cache --virtual libssl-dev libffi-dev python-dev make gcc g++ musl-dev
RUN pip install cython
RUN pip install -r requirements.txt
RUN apk del libssl-dev libffi-dev python-dev make gcc g++ musl-dev

### Stage 4: Run application ###
CMD ["gunicorn", "-w 4", "api.wsgi:app"]
