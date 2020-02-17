#!/bin/bash

docker-compose up -d
docker-compose logs > test.logs
docker-compose down
cat test.logs

