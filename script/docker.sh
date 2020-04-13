#!/bin/bash
curl https://get.docker.com | sudo bash
source ~/.bashrc
sudo usermod -aG docker ${USER}
su - ${USER}
docker stack deploy --compose-file docker-compose.yml superherostack 