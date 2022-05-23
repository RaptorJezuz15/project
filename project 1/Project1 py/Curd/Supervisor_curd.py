from abc import ABC, abstractmethod


class SupervisorCurd(ABC):
    @abstractmethod
    def create_supervisor(self, supervisor):
        pass

    @abstractmethod
    def get_supervisor(self, supervisor_n):
        pass

    @abstractmethod
    def get_supervise(self, supervise):
        pass

    @abstractmethod
    def update_supervisor(self, change):
        pass

    @abstractmethod
    def delete_supervisor(self, supervisor):
        pass

    @abstractmethod
    def delete_supervise(self, supervise):
        pass
