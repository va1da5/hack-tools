FROM node:15-alpine3.10 AS build

WORKDIR /src

COPY . .

RUN npm install
RUN npx ng build --prod


FROM nginx:mainline-alpine AS release

EXPOSE 8000

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /src/dist/frontend /usr/share/nginx/html
