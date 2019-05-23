this is python3-flask-mongodb-webapp in docker

python flask
pymongo


use docker-compose to connect db container

0.install docker and start it
docker

1.create external db folder
docker volume create --name=mydbfolder

2.build image first
docker-compose build

3.start docker-pymode,docker-mongodb
docker-compose up -d

4.stop dokcers
doker-compse stop

5.remove these containers
docker-compose rm

6.find these image & delete
docker rmi ***

7. rebuild image and run containers the data should still in db, cause use docker-volumes