#!/bin/bash

  docker run --name local-postgres -v /home/simonb/Services/POSTGRES:/var/lib/postgresql/data -e -p 5432:5432 POSTGRES_PASSWORD=mysecretpassword -d postgres:latest