from Repo.Employee_repo import EmployeeRepo


class EmployeeService:
    def __init__(self, employee_repo: EmployeeRepo):
        self.employee_repo = employee_repo

    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)

    def get_employee(self, employee_id):
        return self.employee_repo.get_employee(employee_id)

    def update_employee(self, employee_id):
        return self.employee_repo.update_employee(employee_id)

    def delete_employee(self, employee_id):
        return self.employee_repo.delete_employee(employee_id)

    def get_employees(self):
        return self.employee_repo.get_employees()
