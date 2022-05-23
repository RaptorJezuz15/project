class Employee:

    def __init__(self,employee_id=0, first_name="", last_name="", email="", password=""):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return str({
            'Employee_ID': self.employee_id,
            'First_Name': self.first_name,
            'Last_Name': self.last_name,
            'Email': self.email,
            "Password": self.password
        })

    def json(self):
        return {
            'EmployeeID': self.employee_id,
            'FirstName': self.first_name,
            'LastName': self.last_name,
            'Email': self.email,
            "Password": self.password
        }