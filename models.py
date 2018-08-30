# -*- coding: utf-8 -*-


class Order(object):
    def __init__(self, id=None, client_id=None, products=[]):
        self.id = id
        self.client_id = client_id
        self.products = products


class User(object):
    def __init__(self, name, email):
        self.id = email
        self.name = name
        self.email = email

    def __str__(self):
        return "User(id='%s')" % self.id
