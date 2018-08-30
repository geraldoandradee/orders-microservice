# -*- coding: utf-8 -*-


class InvalidFieldException(Exception):
    pass


class PreconditionFailException(Exception):
    pass


class ItemNotFoundException(Exception):
    pass


class OrderAlreadyExistsException(Exception):
    pass


class InvalidProductException(Exception):
    pass
