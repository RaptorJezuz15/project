class Supervisor:

    def __init__(self, supervisor_n="", supervise=0):
        self.supervisor_n = supervisor_n
        self.supervise = supervise

    def __repr__(self):
        return str({
            'supervisor': self.supervisor_n,
            'supervise': self.supervise
        })

    def json(self):
        return {
            'supervisor': self.supervisor_n,
            'supervise': self.supervise
        }
