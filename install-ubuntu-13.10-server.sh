# Install ddmi (and docker) on Ubuntu 13.10
# Author: Nate Ferrero

# Usage:
# curl https://github.com/NateFerrero/ddmi/blob/master/install-ubuntu-13.10-server.sh | sh

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

# install docker-py
sudo apt-get install -y python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install docker-py
