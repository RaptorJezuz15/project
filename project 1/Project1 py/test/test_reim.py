import unittest
from unittest.mock import MagicMock
from Class.Reimburstment import Reimburstment
from Repo.Reimburstment_Repo import ReimburstmentRepo
from Services.Reimburstment_Service import ReimburstmentService

rr = ReimburstmentRepo()
rs = ReimburstmentService(rr)


class TestReimService(unittest.TestCase):

    def test_get_reim(self):
        rs.get_reimburstment = MagicMock(return_value=[
            Reimburstment(case_id=1, reim_amount=489, request_date=1651698098, grade="A", employee=1, supervisor="HM89",
                          event_des="certificate", status="await further approval"),
            Reimburstment(case_id=2, reim_amount=1000, request_date=1651698098, grade="B", employee=3,
                          supervisor="HM89",
                          event_des="Graduated", status="pending"),
            Reimburstment(case_id=4, reim_amount=1000, request_date=0, grade="B", employee=3,
                          supervisor="HM89", event_des="Graduated", status="pending")
        ])

        refined_reim = rs.get_reimburstment(4)
        print(refined_reim)

        self.assertListEqual(refined_reim, [
            Reimburstment(case_id=1, reim_amount=489, request_date=1651698098, grade="A", employee=1, supervisor="HM89",
                          event_des="certificate", status="await further approval"),
            Reimburstment(case_id=2, reim_amount=1000, request_date=1651698098, grade="B", employee=3,
                          supervisor="HM89",
                          event_des="Graduated", status="pending")
        ])


if __name__ == '__main__':
    print("hello")
