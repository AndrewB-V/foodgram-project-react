# build env
FROM node:14-alpine as build-stage
WORKDIR     /app

ADD         https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait ./wait
RUN         chmod +x ./wait

COPY        package.json yarn.lock ./
RUN         yarn
COPY        . ./
RUN         yarn build


FROM        nginx:stable-alpine
COPY        --from=build-stage /app/build/ /usr/share/nginx/html
COPY        --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf
