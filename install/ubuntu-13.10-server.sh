# Install ddmi (and docker) on Ubuntu 13.10
# Author: Nate Ferrero

# Usage:
# curl https://raw.github.com/NateFerrero/ddmi/master/install/ubuntu-13.10-server.sh | sh

# AUFS filesystem support
sudo apt-get update
sudo apt-get install -y linux-image-extra-`uname -r`

# Add the Docker repository key to your local keychain
# using apt-key finger you can check the fingerprint matches
# 36A1 D786 9245 C895 0F96 6E92 D857 6A8B A88D 21E9
sudo sh -c "wget -qO- https://get.docker.io/gpg | apt-key add -"

# Add the Docker repository to your apt sources list.
sudo sh -c "echo deb http://get.docker.io/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"

# update
sudo apt-get update

# install docker
sudo apt-get install -y lxc-docker

# Add current user to docker group
sudo usermod -a -G docker $(whoami)

# install docker-py
sudo apt-get install -y python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install docker-py

# Restart the docker daemon
sudo service docker restart

# Download an ubuntu image
sudo docker pull ubuntu

# logout
echo "Install complete!"
echo "You should logout before using the docker command in non-root mode."
echo "Try docker: sudo docker run ubuntu echo 'Hello World'"
