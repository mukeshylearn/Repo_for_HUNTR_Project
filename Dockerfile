FROM node:21-alpine
RUN apk update
RUN apk add git
RUN git clone https://github.com/heroku/node-js-getting-started.git
WORKDIR node-js-getting-started
RUN npm install
CMD ["npm" , "start"]