# PingPong
Set up two docker containers to speak to eachother

This repository contains two basic web services built using Flask that are intended to talk to eachother from inside separate containers using docker network. The ping service will send a request to the pong service, and return 'ping ... pong' if successful. 

Relevant docker commands:
```cd ~/ping
docker build -t ping-service .
docker run --name ping-service-container -p 5000:5000 ping-service

cd ../pong
docker build -t pong-service .
docker run --name pong-service-container -p 5001:5001 pong-service

docker network create ping-pong-network
docker network connect ping-pong-network ping-service-container
docker network connect ping-pong-network pong-service-container

docker network inspect ping-pong-network

curl localhost:5000/ping -s
```

This should return
```
$ curl localhost:5000/ping -s

ping ... pong

```