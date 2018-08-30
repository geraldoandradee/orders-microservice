# -*- coding: utf-8 -*-

import logging

from flask import request
from flask_restful import Resource

from flask_jwt import jwt_required
from exceptions import PreconditionFailException
from services import OrderService


class OrderHandler(Resource):

    def __init__(self):
        self.service = OrderService()
        super(OrderHandler, self).__init__()

    @staticmethod
    def _error_message(message, reason, status_code):
        return {"message": message, "reason": reason}, status_code

    @jwt_required()
    def get(self, id=None):
        if id is None:
            return self.service.list()
        else:
            item = self.service.read(id)
            if not item:
                return {}, 404
            return item

    @jwt_required()
    def post(self):
        data = request.get_json()
        try:
            item = self.service.create(data)
            return item, 200
        except Exception as e:
            logging.error("Cannot create a new Product %s" % e)
            return {"message": "Cannot create a new Product", "reason": "Unknown reason."}, 400

    @jwt_required()
    def delete(self, id=None):
        try:
            self.service.delete(id)
        except PreconditionFailException as e:
            logging.error("Cannot delete data: %s" % e)
            return {"message": "You must provide an id to delete"}, 412
        except Exception as e:
            logging.error("Cannot delete data: %s" % e)

        return {}, 200
