import unittest
from unittest.mock import MagicMock
from Class.Employee import Employee
from Repo.Employee_repo import EmployeeRepo
from Services.Empolyee_service import EmployeeService

er = EmployeeRepo()
es = EmployeeService(er)
test_emp = Employee(0, "testname", "testlast", "testmail", "testpass")


class TestEmployeeService(unittest.TestCase):

    def test_a_create_emp(self):
        test = es.get_employee(test_emp)
        assert test.email != "testmail"

    def test_b_get_reim(self):
        get_emp = es.get_employee(test_emp.employee_id)
        print(get_emp.employee_id)
        print(test_emp.employee_id)
        assert get_emp.employee_id == test_emp.employee_id


if __name__ == '__main__':
    unittest.main()
