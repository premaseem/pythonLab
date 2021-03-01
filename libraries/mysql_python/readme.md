# install mysql driver for python 
$ python -m pip install mysql-connector-python

# Connecting mysql via container
$ docker exec -it prem-mysql bash
$ mysql -h localhost -P 3306 -u root -p


####### docker details ############

# pull image 
docker pull mysql


# deploy container with your data dir mounted and port mapping with default password
docker run --name prem-mysql -p 3306:3306 -v /Users/asee2278/docker/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:latest
docker run --name <some-mysql> -e MYSQL_ROOT_PASSWORD=<my-secret-pw> -d mysql:tag

# connect container  
docker exec -it <some-mysql> bash

# check logs 
docker logs <some-mysql>

####### docker details ############
