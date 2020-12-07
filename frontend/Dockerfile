FROM node:12.13.0-alpine as build 
RUN mkdir /app
WORKDIR /app
COPY ./angularFront package*.json ./
RUN npm install 
COPY ./angularFront .
RUN npm run build

FROM nginx 
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/angularFront /usr/share/nginx/html
