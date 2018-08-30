# -*- coding: utf-8 -*-

import os
import requests
import json
from exceptions import InvalidProductException, ItemNotFoundException

"""
This is a strong candidate to make a separate library.

I won't do that but because I do not have enough to make it rigth: in a separate repository, well tested  
 
"""


class BaseProductClient(object):
    def get_token(self):
        response = requests.post(''.join([self.product_api, '/v1/auth']), headers={'Content-Type': 'application/json'},
                                 data=json.dumps({"username": self.product_user, "password": self.product_password}))
        data = response.json()
        return data['access_token']


class ProductClient(BaseProductClient):

    def __init__(self, product_api=None, product_user=None, product_password=None):
        self.product_api = product_api or os.getenv('PRODUCT_API_HOST')
        self.product_user = product_user or os.getenv('PRODUCT_API_USER')
        self.product_password = product_password or os.getenv('PRODUCT_API_PASS')

    def get_product(self, product_id):
        token = self.get_token()
        response = requests.get(''.join([self.product_api, '/v1/products/', str(product_id)]),
                                headers={"Authorization": "JWT %s" % token, 'Content-Type': 'application/json'})
        if response.status_code == 404:
            raise ItemNotFoundException("Product does not exists.")
        elif response.status_code != 200:
            raise InvalidProductException("Cannot validate this product.")

        return response.json()
