#!/bin/bash

# Update and upgrade the system
apt-get update
apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Install Git
sudo apt install git -y

# Clone Duckling
git clone https://github.com/eliottbourrigan/duckling
cd duckling

# Build and run the container
sudo docker build -t duckling .
sudo docker run -p 80:80 duckling