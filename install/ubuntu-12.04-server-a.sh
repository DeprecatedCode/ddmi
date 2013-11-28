# Install ddmi (and docker) on Ubuntu 12.04 - Part A
# Author: Nate Ferrero

# Usage:
# curl https://raw.github.com/NateFerrero/ddmi/master/install/ubuntu-12.04-server-a.sh | sh

# install the backported kernel
sudo apt-get update
sudo apt-get install linux-image-generic-lts-raring linux-headers-generic-lts-raring

# reboot
sudo reboot
