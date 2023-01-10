#!/usr/bin/python3
"""a module that converts a dictionary ti json file"""
import json


def to_json_string(my_obj):
    """ amethod that returns the json representation of a string"""

    return json.dumps(my_obj)
