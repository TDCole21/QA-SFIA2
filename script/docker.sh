#!/bin/bash
# curl https://get.docker.com | sudo bash
source ~/.bashrc
# sudo usermod -aG docker ${USER}
# sudo su - ${USER}
docker stack deploy --compose-file docker-compose.yml superherostack 