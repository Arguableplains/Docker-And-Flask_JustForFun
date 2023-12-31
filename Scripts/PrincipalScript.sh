#!/bin/bash

echo "START - OnLinux"

echo "Initializing Database Container and Configs"
# Docker SQL commands
sudo docker pull mysql:latest
sudo docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
sleep 10

# Docker SQL Command Verification - Creating
if [ $? -ne 0 ]; then
    sudo docker rm -f mysql-container
    echo "There was an error while creating and starting the container"
    exit 1
fi

# Docker copying command - the Database Script to Mysql container
sudo docker cp ./../Database/DatabaseBooks.sql mysql-container:/

# Docker execution - populating the created Database inside Mysql container
sudo docker exec mysql-container sh -c 'mysql -u root -proot mysql <  ./DatabaseBooks.sql'

# Docker SQL Command Verification - Executing Script SQL
if [ $? -ne 0 ]; then
    sudo docker rm -f mysql-container
    echo "There was an error while running the SQL script into the Database Container"
    exit 1
fi

echo "The SQL Container creation was successful"
sleep 5

echo "Initializing Main API Container"

# Docker API commands

# Docker build - building the main image
sudo docker build -t the-sql-python-api-image ./..

# Docker SQL Command Verification - Executing Script
if [ $? -ne 0 ]; then
    sudo docker image rm the-sql-python-api-image
    echo "There was an error while creating the API image"
    exit 1
fi

# Request for web port to be used
echo "Enter the web port for connections and requests to the API:"
read WEB_PORT

# Docker Run - Starting the main Python Container
sudo docker run -p $WEB_PORT:5000 --link mysql-container --name pythonapi -d the-sql-python-api-image

# Docker SQL Command Verification - Executing Script
if [ $? -ne 0 ]; then
    sudo docker rm -f pythonapi
    sudo docker image rm the-sql-python-api-image
    echo "There was an error while creating and starting the API Container"
    exit 1
fi

# When everything is successful
echo "The API Container creation was successful"
echo "END - Everything was successful"


