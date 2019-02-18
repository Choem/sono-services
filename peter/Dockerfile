### Stage 1: Build ###
FROM node:10-alpine as builder
WORKDIR /server

COPY . /server

RUN npm install

RUN npm run build

### Stage 2: Run ###
FROM keymetrics/pm2:latest-alpine

# Bundle APP files
COPY --from=builder server/dist ./
COPY package.json .
COPY pm2.json .

# Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install --production

# Show current folder structure in logs
# RUN ls -al -R

CMD [ "pm2-runtime", "start", "pm2.json" ]
