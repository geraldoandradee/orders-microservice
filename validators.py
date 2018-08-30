# -*- coding: utf-8 -*-
import logging

from clients import ProductClient
from exceptions import InvalidFieldException, ItemNotFoundException, InvalidProductException
from repository import VALID_CLIENTS_DATA


class OrderValidator(object):
    def __init__(self, data):
        self.data = data
        self.possible_fields = ['id', 'client_id', 'products']
        self.errors = []

    def is_valid_fields(self, field):
        if field not in self.possible_fields:
            raise InvalidFieldException("Order has not '%s' field" % field)
        return True

    def validate(self, is_a_patch=False):
        if not is_a_patch:
            for field in self.possible_fields:
                if field not in self.data.keys():
                    raise InvalidFieldException("You must provide a '%s' field" % field)

        for key, value in self.data.items():
            if self.is_valid_fields(key):
                getattr(self, ''.join(['_validate_', key]))(key, value)

    def _validate_id(self, key, value):
        try:
            int(value)
        except ValueError as e:
            logging.error("Invalid '%s' field: %s" % (key, e))
            raise InvalidFieldException("Invalid '%s' field")

    def _validate_client_id(self, key, value):
        if not value:
            raise InvalidFieldException("A Client ID must have a %s" % key)

        # here I pretend to call a external service to validate client
        if value not in VALID_CLIENTS_DATA.keys():
            raise InvalidFieldException("A Order must have a valid client")

    def _validate_products(self, key, product_ids):
        if len(product_ids) < 1:
            raise InvalidFieldException("A Order must have at least one product")

        for product_id in product_ids:
            self._validate_product(product_id)

    def _validate_product(self, product_id):
        client = ProductClient()

        try:
            client.get_product(product_id)
            return True
        except ItemNotFoundException as e:
            logging.error("Product was not found: %s" % e)
        except InvalidProductException as e:
            logging.error("Cannot validate Product: %s" % e)

        return False
