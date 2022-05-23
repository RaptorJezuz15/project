from datetime import datetime


class Reimburstment:

    def __init__(self,case_id=0, reim_amount=0, request_date='', grade="C", employee=0, supervisor="", event_des="",
                 status="pending"):
        self.case_id = case_id
        self.reim_amount = reim_amount
        self.request_date = request_date
        self.grade = grade
        self.employee = employee
        self.supervisor = supervisor
        self.event_des = event_des
        self.status = status

    def __repr__(self):
        return str({
            'case_id': self.case_id,
            'reimbursement_amount': self.reim_amount,
            'due_date': self.request_date,
            'grade': self.grade,
            'employee': self.employee,
            'supervisor': self.supervisor,
            'event_description': self.event_des,
            'status': self.status
        })

    def json(self):
        return {
            'caseId': self.case_id,
            'reimbursementAmount': self.reim_amount,
            'requestDate': self.request_date,
            'grade': self.grade,
            'employee': self.employee,
            'supervisor': self.supervisor,
            'eventDescription': self.event_des,
            'status': self.status
        }