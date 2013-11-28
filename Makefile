.PHONY: install

install:
	sudo apt-get install -y python-pip
	sudo pip install -r requirements.txt
	sudo python setup.py install
	# sudo service ddmi restart

run:
	sudo python setup.py install
	ddmi-server

dev:
	python -m ddmi.app
