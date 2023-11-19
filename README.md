Task 1 
Write a Dockerfile for the nodeJS application ( https://github.com/heroku/node-js-getting-started ). Make sure to use all the Best Practices for Docker, it will be evaluated.

Solution - 
Wrote Dockerfile to build the image. 
Below command could be execute to build the image
#docker build -t my-nodejs-app .

Task 2
Prepare a docker-compose with Loki, Grafana, Promtail, and nodeJS application ( https://github.com/heroku/node-js-getting-started ). Set up a log collection from the nodeJS application.

Solution -
Wrote a docker-compose.yml to run conatainers of Loki, Grafana, Promtail and nodeJS application.
Nodejs application is running on 5001 but exposed on 5000.
Loki is running 
