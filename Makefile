.PHONY: install

install:
	sudo apt-get install -y python-pip
	sudo pip install -r requirements.txt
	sudo python setup.py install
	# sudo service ddmi restart

reset:
	sudo rm -vf /var/lib/ddmi/ddmi-data
	sudo rm -vf /var/lib/ddmi/ddmi-id
	echo "Reset DDMI"

run:
	sudo python setup.py install
	ddmi-server

dev:
	python -m ddmi.app
