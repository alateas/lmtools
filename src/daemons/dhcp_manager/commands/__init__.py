from model import DhcpModel

class Command(object):
    def __init__(self):
        self._model = DhcpModel()
    
    def call(self, params=[]):
        return None

class LeasesGetAll(Command):
    def call(self, params=[]):
        return self._model.get_pb_all_leases()

class LeasesGetRange(Command):
    def call(self, params):
        return self._model.get_pb_leases_by_range(params[0], params[1])

class CreateLease(Command):
    def call(self, params):
        return self._model.pb_create_lease(params[0], params[1], params[2])