#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
    and then save them to a file:"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# store in variable the name of the output file
filename = "add_item.json"
# check if the file exists
try:
    # if file exists load ints elements into the list
    lst = load_from_json_file(filename)
except:
    # if file does not exist or is empty, create empty list
    lst = []
# go through all arguments and appends them to the list
for element in sys.argv[1:]:
    lst.append(element)

# save the list into the file as a JSON representation
save_to_json_file(lst, filename)
