#!/bin/bash

docker-compose up -d crypto_analyser_mariadb && docker-compose run --rm crypto_analyser
