#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from handlers import OrderHandler
from security import verify, identity

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'm9ruhppNu4OHQCtrsoez8woU')
app.config['JWT_AUTH_URL_RULE'] = os.getenv('JWT_AUTH_URL_RULE', '/v1/auth')
app.config['JWT_LEEWAY'] = os.getenv('JWT_LEEWAY', 60)  # 60 seconds

api = Api(app, prefix="/v1")

jwt = JWT(app, verify, identity)

api.add_resource(OrderHandler, '/orders', '/orders/<int:id>')
