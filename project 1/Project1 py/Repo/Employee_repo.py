from Class.Employee import Employee
from Project1_db import connection
from Curd.Employee_curd import EmployeeCurd


def build_employee(record):
    return Employee(employee_id=record[0], first_name=record[1], last_name=record[2], email=record[3],
                    password=record[4])


class EmployeeRepo(EmployeeCurd):
    def create_employee(self, employee):
        sql = 'INSERT INTO employee VALUES(DEFAULT,%s,%s,%s, %s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [employee.first_name, employee.last_name, employee.email, employee.password])

        connection.commit()
        record = cursor.fetchone()

        return build_employee(record)

    def get_employee(self, employee_id):
        sql = 'SELECT * FROM employee WHERE employeeid=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        return build_employee(record)

    def get_employees(self):
        sql = 'SELECT * FROM employee'
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        account_list = [build_employee(record) for record in records]

        return account_list

    def update_employee(self, change):
        sql = 'UPDATE employee SET firstname=%s, lastname=%s, email=%s, password=%s where employeeid=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [change.first_name, change.last_name, change.email, change.password, change.employee_id])
        connection.commit()
        record = cursor.fetchone()

        return build_employee(record)

    def delete_employee(self, employee_id):
        sql = 'DELETE FROM employee WHERE employeeid=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])

        connection.commit()
        record = cursor.fetchone()

        return build_employee(record)


def _test():
    er = EmployeeRepo()
    emp = Employee(first_name="Micheal", last_name="Campbell", email="Benco@gmail.com", password="pass123")
    print(er.create_employee(emp))


if __name__ == '__main__':
    _test()
