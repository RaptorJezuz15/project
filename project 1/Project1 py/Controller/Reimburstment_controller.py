from flask import jsonify, request
from werkzeug.exceptions import abort

from Class.Reimburstment import Reimburstment
from Repo.Reimburstment_Repo import ReimburstmentRepo
from Services.Reimburstment_Service import ReimburstmentService
from exceptions.resource_not_found import ResourceNotFound

rr = ReimburstmentRepo()
rs = ReimburstmentService(rr)


def route(app):
    @app.route("/reimburstment/<case_id>", methods=['GET'])
    def get_reimburstment(case_id):
        try:
            return jsonify(rs.get_reimburstment(case_id).json(), 200)
        except ValueError:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reimburstment/1/<supervisor>", methods=['GET'])
    def get_super(supervisor):
        try:
            return jsonify([reimburstment.json() for reimburstment in rs.get_super(supervisor)])
        except ValueError:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reimburstment/<employee>", methods=["POST"])
    def post_reimburstment(employee):
        try:
            body = request.json

            reimburstment = Reimburstment(grade=body['grade'], employee=employee,
                                          supervisor=['supervisor'], event_des=body['eventDescription'])
            reimburstment = rs.create_reimburstment(reimburstment)
            return reimburstment.json()
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reimburstment/<case_id>", methods=["PUT"])
    def put_reimburstment(case_id):
        body = request.json
        reimburstment = Reimburstment(case_id=case_id, reim_amount=body["reimAmount"], request_date=body['requestDate'],
                                      status=body['status'])
        reimburstment = rs.update_reimburstment(reimburstment)
        return reimburstment.json()

    @app.route('/reimburstment/<case_id>', methods=["DELETE"])
    def delete_reimburstment(case_id):
        try:
            rs.delete_reimburstment(case_id)
            return 'Delete successful', 204  # No Content
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/reimburstment/<case_id>', methods=['PATCH'])
    def patch_reimburstment(case_id):
        try:
            body = request.json
            amount = float(body['amount'])
            return rs.request_reimburstment(case_id, amount).json()
        except ValueError:
            return "Not a valid ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/reimburstment/1/<case_id>', methods=['PATCH'])
    def patch_stat(case_id):
        body = request.json
        stat = body['status']
        return rs.reimburstment_status(case_id, stat)

    @app.route("/reimburstment", methods=['GET'])
    def get_all_reim():
        return jsonify([reimburstment.json() for reimburstment in rs.get_all_reim()])
