#!/bin/bash

  docker run --name local-postgres -p 5432:5432 -v /home/simonb/Services/POSTGRES:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpassword -d postgres:latest