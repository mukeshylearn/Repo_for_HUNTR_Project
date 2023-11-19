Task 1 

Write a Dockerfile for the nodeJS application ( https://github.com/heroku/node-js-getting-started ). Make sure to use all the Best Practices for Docker, it will be evaluated.

Solution - 
Written Dockerfile to build the image. 
Below command could be used to build the image
#docker build -t my-nodejs-app .

Task 2
Prepare a docker-compose with Loki, Grafana, Promtail, and nodeJS application ( https://github.com/heroku/node-js-getting-started ). Set up a log collection from the nodeJS application.

Solution -
Written a docker-compose.yml to run conatainers of Loki, Grafana, Promtail and nodeJS application.
Created the network as app.
Nodejs application is running on 5001 but exposed on 5000.
Loki is running on 3100 port.
Config files for Promtail and Grafana are avilable in config directory.
Grafana is running on 3000 port.

Command to run docker-compose and create containers
#docker-compose up -d

Task 3 
Write a simple script (in any language) that will print the numbers from 0 to 100 and convert every tenth to a wordy version.

Solution -
Written a script in python as tenthNoInWordsRange100.py
#python3 tenthNoInWordsRange100.py
