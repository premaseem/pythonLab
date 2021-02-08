## Mongo db docker setup

# look existing images in system
docker images | grep mongo

# pull docker image
docker pull mongo

# Create a /mongodata directory on the host system
mkdir -p ~/mongodata

# Start the Docker container with the run command using the mongo image. The /data/db directory in the container is mounted as /mongodata on the host.
docker run -it -v ~/mongodata:/data/db -p 27017:27017 --name mongodb -d mongo
# -it ( run terminal iteractive mode)
# -p 27017:27017 (port mapping)
# -v mongodata:/data/db ( data volume mount)
# --name mongodb ( container name or tag)
# -d run in detached mode / background

# check logs onf container : docker logs <container name>
docker logs mongodb

# connect to docker container bash : docker exec -it <container name> bash
docker exec -it mongodb bash

# list out docker containers
docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}"

# remove all docker images
#docker image prune -a

