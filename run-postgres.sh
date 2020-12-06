#!/bin/bash

  docker network create udacity-net
  docker run --name local-postgres --network udacity-net --publish 5432:5432 \
         -v /home/simonb/Services/POSTGRES:/var/lib/postgresql/data -e POSTGRES_USER=student \
         -e POSTGRES_PASSWORD=student -d postgres:latest
