#!/bin/bash

  docker run --network host --name local-postgres --rm -d --ipc=host \
         -v /home/simonb/Services/POSTGRES:/var/lib/postgresql/data -v /var/run/postgresql/:/var/run/postgresql \
	 -e POSTGRES_USER=student -e POSTGRES_PASSWORD=student -e POSTGRES_DB=studentdb -d "postgres:latest"
