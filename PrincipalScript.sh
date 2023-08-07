#!/bin/bash

echo "START"

echo "Initializing Database Container and Configs"
#Docker SQL commands
sudo docker pull mysql:latest
sudo docker run --name mysql-container -e MYSQL_ROOT_PASSORD=root -d mysql:latest
sudo docker exec -i mysql-container mysql -u root -p sys < ./DatabaseBooks.sql

echo "Initializing Main API Container"
#Docker API commands
sudo docker build -t the-sql-python-api-image .
sudo docker run -p 9000:5000 --link mysql-container --name pythonapi -d the-sql-Python-api-image

echo "END"


