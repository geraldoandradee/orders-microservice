# -*- coding: utf-8 -*-
from models import User
from repository import USER_DATA


################################################################################
# START OF "auth-microservice"
# Hi, guys. I'll leave this part as is. But do not think it is a mess intended.
# Think in this portion of code as a auth-microservice. Due my limited time and
# my actual moment in my current work I won't build a auth-microservice.
#
# We can discuss it later ;)
#

def verify(username, password):
    """
    Here inside this function I'm suppose to call a auth-microservice. But for
    reasons I already said let's mock it up.

    :param username:
    :param password:
    :return: bool|mixed
    """
    if not (username and password):
        return False

    if USER_DATA.get(username) == password:
        return User(name="Geraldo Andrade", email='geraldo@geraldoandrade.com')

    return False


# END OF "auth-microservice"
################################################################################

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}
