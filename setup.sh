#!/bin/bash

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Clone Duckling
git clone https://github.com/eliottbourrigan/duckling
cd duckling

# Build and run the container
docker build -t duckling .
docker run -p 80:80 duckling