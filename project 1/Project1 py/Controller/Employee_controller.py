from flask import jsonify, request
from werkzeug.exceptions import abort

from Class.Employee import Employee
from Repo.Employee_repo import EmployeeRepo
from Services.Empolyee_service import EmployeeService
from exceptions.resource_not_found import ResourceNotFound

er = EmployeeRepo()
es = EmployeeService(er)


def route(app):
    @app.route("/employee/<employee_id>", methods=['GET'])
    def get_employee(employee_id):
        try:
            return jsonify(es.get_employee(employee_id).json(), 200)
        except ValueError:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee", methods=["POST"])
    def post_employee():
        body = request.json

        employee = Employee(first_name=body["firstName"], last_name=body['lastName'], email=body['email'],
                            password=body['password'])
        employee = es.create_employee(employee)
        return employee.json()

    @app.route("/employee/<employee_id>", methods=["PUT"])
    def put_employee(employee_id):
        body = request.json
        employee = Employee(employee_id=employee_id, first_name=body["firstName"], last_name=body['lastName'],
                            email=body['email'], password=body['password'])
        employee = es.update_employee(employee)
        return employee.json()

    @app.route('/employee/<employee_id>', methods=["DELETE"])
    def delete_employee(employee_id):
        employee = es.delete_employee(employee_id)
        if employee:
            return 'Delete successful', 204  # No Content
        else:
            abort(422, "Employee id wasn't found")

    @app.route("/employees", methods=['GET'])
    def get_employees():
        return jsonify([employee.json() for employee in es.get_employees()])
