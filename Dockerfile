FROM node:14-alpine AS build

RUN apk add --no-cache --virtual .gyp python3 make g++

WORKDIR /app
ENV NODE_ENV=production

# COPY package.json yarn.lock ./
COPY package.json package-lock.json ./
RUN yarn --frozen-lockfile --non-interactive

COPY . .
RUN yarn build

FROM nginx:alpine

COPY --from=build --chown=nginx:nginx /app/public /usr/share/nginx/html
