ddmi
====

Distributed Docker Management Interface

## Strategy

Each node in the network runs a copy of ddmi. It is possible to then connect multiple instances of ddmi together through the web ui, and manage all docker servers in the pool.

## Quick Install

Please see the install/*.sh script for your (Ubuntu only for now) operating system.

## Manual Install

Ensure you have docker and pip, then:

```bash
sudo pip install ddmi
```

If you do not want to install ddmi via pip, you will need to run setup:

```python
python setup.py install
```

## Running ddmi

Start the service in the console:

```bash
ddmi-server
```

Start the service with upstart:

```bash
sudo service ddmi start
```

Start the service in dev mode:

```bash
make dev
```

Finally, visit `http://<server-hostname-or-ip>:4244` in your browser.