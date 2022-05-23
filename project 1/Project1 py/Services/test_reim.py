import unittest
from unittest.mock import MagicMock
from Class.Reimburstment import Reimburstment
from Repo.Reimburstment_Repo import ReimburstmentRepo
from Services.Reimburstment_Service import ReimburstmentService

rr = ReimburstmentRepo()
rs = ReimburstmentService(rr)

test_reim = Reimburstment(0, 0, 0, "A", 0, "testsup", "testgrade", "teststat")


class TestReimService(unittest.TestCase):

    def test_a_create_reim(self):
        test = rs.create_reimburstment(test_reim)
        assert test.status != "teststat"

    def test_b_get_reim(self):
        get_form = rs.get_reimburstment(test_reim.case_id)
        print(get_form.employee_id)
        print(test_reim.case_id)
        assert get_form.case_id == test_reim.case_id


print("hello")
