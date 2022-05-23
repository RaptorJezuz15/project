from Repo.Supervisor_repo import SupervisorRepo
from Services.Reimburstment_Service import ReimburstmentService


class SupervisorService:
    def __init__(self, supervisor_repo: SupervisorRepo):
        self.SupervisorRepo = supervisor_repo

    def create_supervisor(self, supervisor):
        return self.SupervisorRepo.create_supervisor(supervisor)

    def get_supervisor(self, supervisor_n):
        return self.SupervisorRepo.get_supervisor(supervisor_n)

    def get_supervise(self, supervise):
        return self.SupervisorRepo.get_supervise(supervise)

    def update_supervisor(self, supervisor_n):
        return self.SupervisorRepo.update_supervisor(supervisor_n)

    def delete_supervisor(self, supervisor_n):
        return self.SupervisorRepo.delete_supervisor(supervisor_n)

    def delete_supervise(self, supervise):
        return self.SupervisorRepo.delete_supervise(supervise)

    # def grade(self,):

