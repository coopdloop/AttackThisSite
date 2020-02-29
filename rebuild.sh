echo 'Delete container, delete volume and then bring back up..'
docker stop $(docker ps -f name=cooper-lab1 -q)
docker rm $(docker ps -f name=cooper-lab1 -a -q)
docker-compose up --build