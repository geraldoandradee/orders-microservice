# -*- coding: utf-8 -*-
from exceptions import OrderAlreadyExistsException, PreconditionFailException
from models import Order
from repository import db
from validators import OrderValidator


class OrderService(object):

    def _validate(self, payload, is_a_patch=False):
        validator = OrderValidator(payload)
        validator.validate(is_a_patch)

    def create(self, payload):
        self._validate(payload)

        if 'id' in payload:
            item = self.read(payload['id'])
            if item:
                raise OrderAlreadyExistsException("Order already exists")
        else:
            raise PreconditionFailException("You must provide an ID")

        product = Order()
        product.__dict__.update(payload)
        db.save(payload)

        return self.read(payload['id'])

    def read(self, id, klass_reference=None):
        return db.get(id, klass_reference)

    def delete(self, id):
        if id:
            return db.delete(id)
        raise PreconditionFailException("You must provide an id for deletion")
