#!/bin/bash

  docker run --name local-postgres -v /home/simonb/Services/POSTGRES:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpassword -d postgres:latest