#!/usr/bin/python3
"""module for addng an item"""
import json
import os.path
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my = "add_item.json"
json = []

if os.path.exists(my):
    json = load_from_json_file(my)

for arg in range(1, len(sys.argv)):
    json.append(sys.argv[arg])

save_to_json_file(json, my)
