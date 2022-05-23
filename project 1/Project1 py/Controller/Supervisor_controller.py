from flask import jsonify, request
from werkzeug.exceptions import abort

from Class.Supervisor import Supervisor
from Repo.Supervisor_repo import SupervisorRepo
from Services.Supervisor_service import SupervisorService
from exceptions.resource_not_found import ResourceNotFound

sr = SupervisorRepo()
ss = SupervisorService(sr)


def route(app):
    @app.route("/super/<supervisor_n>", methods=['GET'])
    def get_supervisor_n(supervisor_n):
        try:
            return jsonify(ss.get_supervisor(supervisor_n).json(), 200)
        except ValueError:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/super/<supervisor_n>", methods=["POST"])
    def post_supervisor(supervisor_n):
        body = request.json

        supervisor = Supervisor(supervisor_n=supervisor_n, supervise=body['supervise'])
        supervisor = ss.create_supervisor(supervisor)
        try:
            return supervisor.json()
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/super/<supervisor_n>", methods=["PUT"])
    def put_supervisor(supervisor_n):
        body = request.json
        supervisor = Supervisor(supervisor_n=supervisor_n, supervise=body['supervise'])

        supervisor = ss.update_supervisor(supervisor)

        try:
            return supervisor.json()
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/super/<supervisor_n>', methods=["DELETE"])
    def delete_supervisor(supervisor_n):
        supervisor = ss.delete_supervisor(supervisor_n)
        if supervisor:
            return 'Delete successful', 204  # No Content
        else:
            abort(422, "Employee id wasn't found")

    @app.route('/super/<supervise>', methods=["DELETE"])
    def delete_supervise(supervise):
        supervise = ss.delete_supervisor(supervise)
        if supervise:
            return 'Delete successful', 204  # No Content
        else:
            abort(422, "Employee id wasn't found")

