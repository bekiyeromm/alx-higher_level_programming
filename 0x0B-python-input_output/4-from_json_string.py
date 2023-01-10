#!/usr/bin/python3
"""a module that returns an object represented by
JSON script"""
import json


def from_json_string(my_str):
    """a module that returns object represented by jsonscript"""

    return json.loads(my_str)
