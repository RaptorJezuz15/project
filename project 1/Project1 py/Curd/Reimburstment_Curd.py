from abc import ABC, abstractmethod


class ReimburstmentCurd(ABC):
    @abstractmethod
    def create_reimburstment(self, reimburstment):
        pass

    @abstractmethod
    def get_reimburstment(self, case_id):
        pass

    @abstractmethod
    def update_reimburstment(self, change):
        pass

    @abstractmethod
    def delete_reimburstment(self, case_id):
        pass
