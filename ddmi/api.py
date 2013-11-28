import uuid
import dataset
import socket
import commands
import docker

# DDMI Python API
class DDMI:

    def __init__(self):
        lib = '/var/lib/ddmi'

        self.docker = docker.Client()

        self.db = dataset.connect('sqlite:////' + lib + '/ddmi-data')

        # Give this server a unique identifier
        id_file = lib + '/ddmi-id'

        try:
            with open(id_file) as f:
                self.ddmi_id = f.read()
        except IOError:
            with open(id_file, 'w') as f:
                self.ddmi_id = 'ddmi-' + str(uuid.uuid4()).split('-')[0]
                f.write(self.ddmi_id)

        self.domain = socket.getfqdn()

        # Save this instance if not found in database
        if not self.db['servers'].find_one(ddmi_id=self.ddmi_id):
            self.db['servers'].insert({
                "ddmi_id": self.ddmi_id,
                "name": self.domain,
                "address": self.domain,
                "ip": self.ipaddr(),
                "state": "active"
            })

    def ipaddr(self):
        return commands.getoutput("/sbin/ifconfig") \
            .split("\n")[1].split()[1][5:]

    def uptime(self):
        with open('/proc/uptime', 'r') as f:
            return round(float(f.readline().split()[0]))

    def me(self):
        self.update_server()
        return self.prepare_server(
            self.db['servers'].find_one(ddmi_id=self.ddmi_id)
        )

    def servers(self):
        self.update_server()
        return [self.prepare_server(x) for x in self.db['servers']]

    def suspend(self, ddmi_id):
        self.db['servers'].update(
            {"ddmi_id": ddmi_id, "state": "suspended"},
            ['ddmi_id'])

    def resume(self, ddmi_id):
        self.db['servers'].update(
            {"ddmi_id": ddmi_id, "state": "active"},
            ['ddmi_id'])

    def update_server(self):
        data = {
            "ip": self.ipaddr(),
            "ddmi_id": self.ddmi_id,
            "uptime": self.uptime()
        }
        self.db['servers'].update(data, ['ddmi_id'])

    def prepare_server(self, server):
        if not server:
            return None
        server['containers'] = list(self.db['containers'].find(ddmi_id=server['ddmi_id']))
        return server

    def get_containers(self):
        return self.docker.containers()
