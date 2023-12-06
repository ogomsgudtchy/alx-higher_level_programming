#!/usr/bin/python3
"""Defines a str-to-JSON func."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a str object."""
    return json.dumps(my_obj)
