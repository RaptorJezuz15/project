from Curd.Reimburstment_Curd import ReimburstmentCurd
from Project1_db import connection
from Class.Reimburstment import Reimburstment
from exceptions.resource_not_found import ResourceNotFound


def build_reimburstment(record):
    return Reimburstment(case_id=record[0], reim_amount=record[1], grade=record[2], employee=record[3]
                         , supervisor=record[4], event_des=record[5], request_date=record[6], status=record[7])


class ReimburstmentRepo(ReimburstmentCurd):
    def create_reimburstment(self, reimburstment):
        sql = 'INSERT INTO reimburstment VALUES(DEFAULT,DEFAULT,%s,%s, %s, %s, DEFAULT, DEFAULT) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [reimburstment.grade, reimburstment.employee,
                             reimburstment.supervisor, reimburstment.event_des])

        connection.commit()
        record = cursor.fetchone()

        return build_reimburstment(record)

    def get_reimburstment(self, case_id):
        sql = 'SELECT * FROM reimburstment WHERE caseid=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [case_id])
        record = cursor.fetchone()
        if record:
            return build_reimburstment(record)
        else:
            raise ResourceNotFound(f"reimburstment {case_id} not found")

    def update_reimburstment(self, change):
        sql = 'UPDATE reimburstment SET reimamount=%s, requestdate=%s, status=%s where ' \
              'caseid=%s RETURNING * '

        cursor = connection.cursor()
        cursor.execute(sql, [change.reim_amount, change.request_date, change.status,
                             change.case_id])
        connection.commit()
        record = cursor.fetchone()

        if record:
            return build_reimburstment(record)
        else:
            raise ResourceNotFound(f"reimburstment case id not found")

    def delete_reimburstment(self, case_id):
        sql = 'DELETE FROM reimburstment WHERE caseid=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [case_id])

        connection.commit()
        record = cursor.fetchone()

        if record:
            return build_reimburstment(record)
        else:
            raise ResourceNotFound(f"reimburstment {case_id} not found")

    def get_super(self, supervisor):
        sql = "select * from reimburstment inner join employee on reimburstment.supervisor = employee.email where " \
              "reimburstment.supervisor = %s "
        cursor = connection.cursor()
        cursor.execute(sql, [supervisor])

        records = cursor.fetchall()

        account_list = [build_reimburstment(record) for record in records]

        return account_list

    def get_all_reim(self, ):
        sql = "select * from reimburstment"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        account_list = [build_reimburstment(record) for record in records]

        return account_list




def _test():
    # reim = Reimburstment(grade='A', employee=1, supervisor='Harrison Morgan', event_des="certificate")
    rr = ReimburstmentRepo()
    print(rr.get_super("HM89"))


if __name__ == '__main__':
    _test()
