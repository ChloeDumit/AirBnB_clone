#!/usr/bin/python3
""" importing """
from models.base_model import BaseModel

"""
AirBnB Clone
"""


class User(BaseModel):
    """user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
