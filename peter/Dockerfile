### Stage 1: Build ###
FROM keymetrics/pm2:latest-alpine

# Bundle APP files
COPY dist ./
COPY package.json .
COPY pm2.json .

# Install app dependencies
RUN npm install typeorm --no-bin-links
RUN npm install

# Show current folder structure in logs
EXPOSE 3333
EXPOSE 50051

CMD [ "pm2-runtime", "start", "pm2.json" ]
