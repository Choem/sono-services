### Stage 1: Build ###
FROM python:3.7.2-alpine

### Stage 2: Bundle app ###
COPY . /api
COPY . /migrations
COPY .env.template .env
COPY alembic.ini
COPY requirements.txt

### Stage 3: Install requirements ###
RUN pip install -r requirements.txt

### Stage 4: Run application ###
CMD ["gunicorn", "-w 4", "api.wsgi:app"]
