install:
	sudo python setup.py install
	sudo service ddmi restart

run:
	sudo python setup.py install
	ddmi-server