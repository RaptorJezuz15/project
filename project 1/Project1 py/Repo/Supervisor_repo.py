from Class.Supervisor import Supervisor
from Curd.Supervisor_curd import SupervisorCurd
from Project1_db import connection


def build_supervisor(record):
    return Supervisor(supervisor_n=record[0], supervise=record[1])


class SupervisorRepo(SupervisorCurd):
    def create_supervisor(self, supervisor):
        sql = 'INSERT INTO supervisor VALUES(%s,%s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [supervisor.supervisor_n, supervisor.supervise])

        connection.commit()
        record = cursor.fetchone()

        return build_supervisor(record)

    def get_supervisor(self, supervisor_n):
        sql = 'SELECT * FROM supervisor WHERE supervisor=%s'
        cursor = connection.cursor()
        cursor.execute(sql, [supervisor_n])
        record = cursor.fetchone()
        return build_supervisor(record)

    def get_supervise(self, supervise):
        sql = "select * from supervisor inner join employee on supervisor.supervise = employee.employeeid where " \
              "supervisor.supervise = %s "
        cursor = connection.cursor()
        cursor.execute(sql, [supervise])

        records = cursor.fetchall()

        supervise_list = [build_supervisor(record) for record in records]

        return supervise_list

    def update_supervisor(self, change):
        sql = 'UPDATE supervisor SET supervisor=%s, supervise=%s where supervisor=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [change.supervisor, change.supervise])
        connection.commit()
        record = cursor.fetchone()

        return build_supervisor(record)

    def delete_supervisor(self, supervisor_n):
        sql = 'DELETE FROM supervisor WHERE supervisor=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [supervisor_n])

        connection.commit()
        record = cursor.fetchone()

        return build_supervisor(record)

    def delete_supervise(self, supervise):
        sql = 'DELETE FROM supervisor WHERE supervise=%s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, [supervise])

        connection.commit()
        record = cursor.fetchone()

        return build_supervisor(record)


def _test():
    super = Supervisor(supervisor_n="Harrison Morgan", supervise=1)
    sr = SupervisorRepo()
    sr.create_supervisor(super)


if __name__ == '__main__':
    _test()
