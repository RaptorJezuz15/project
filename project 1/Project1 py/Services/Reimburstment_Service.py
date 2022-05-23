from time import time

from Repo.Reimburstment_Repo import ReimburstmentRepo


class ReimburstmentService:

    def __init__(self, reimburstment_repo: ReimburstmentRepo):
        self.reimburstment_repo = reimburstment_repo

    def create_reimburstment(self, reimburstment):
        return self.reimburstment_repo.create_reimburstment(reimburstment)

    def get_reimburstment(self, case_id):
        return self.reimburstment_repo.get_reimburstment(case_id)

    def update_reimburstment(self, case_id):
        return self.reimburstment_repo.update_reimburstment(case_id)

    def delete_reimburstment(self, case_id):
        return self.reimburstment_repo.delete_reimburstment(case_id)

    def get_super(self, supervisor):
        return self.reimburstment_repo.get_super(supervisor)

    def request_reimburstment(self, case_id, amount):
        reim = self.get_reimburstment(case_id)
        reim.request_date = time()

        if amount > 1000:
            reim.reim_amount = 1000
            return self.update_reimburstment(reim)
        else:
            reim.reim_amount = amount
            return self.update_reimburstment(reim)

    def reimburstment_status(self, case_id, stat):
        reim = self.get_reimburstment(case_id)
        reim.status = stat
        self.update_reimburstment(reim)

    def get_all_reim(self):
        return self.reimburstment_repo.get_all_reim()


def _test():
    rr = ReimburstmentRepo()
    rs = ReimburstmentService(rr)
    print(rs.request_reimburstment(1, 400))


if __name__ == '__main__':
    _test()

# if reim.event_des == " University Courses":
#     x = 800
#     if amount > x:
#         reim.reim_amount = x
#         return self.update_reimburstment(reim)
#     else:
#         reim.reim_amount = amount
#         return self.update_reimburstment(reim)
# if reim.event_des == "Seminars ":
#     x = 600
#     if amount > x:
#         reim.reim_amount = x
#         return self.update_reimburstment(reim)
#     else:
#         reim.reim_amount = amount
#         return self.update_reimburstment(reim)
# if reim.event_des == "Certification Preparation Classes":
#     x = 750
#     if amount > x:
#         reim.reim_amount = x
#         return self.update_reimburstment(reim)
#     else:
#         reim.reim_amount = amount
#         return self.update_reimburstment(reim)
# if reim.event_des == "Certification ":
#     x = 1000
#     if amount > x:
#         reim.reim_amount = x
#         return self.update_reimburstment(reim)
#     else:
#         reim.reim_amount = amount
#         return self.update_reimburstment(reim)
# if reim.event_des == "Technical Training ":
#     x = 900
#     if amount > x:
#         reim.reim_amount = x
#         return self.update_reimburstment(reim)
#     else:
#         reim.reim_amount = amount
#         return self.update_reimburstment(reim)
# if reim.event_des == "Other":
#     x = 300
#     if amount > x:
#         reim.reim_amount = x
#         return self.update_reimburstment(reim)
#     else:
#         reim.reim_amount = amount
#         return self.update_reimburstment(reim)
