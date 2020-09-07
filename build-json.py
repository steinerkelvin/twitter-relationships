#!/usr/bin/env python3
import sys
import os
import json

DATA_FOLDER = os.environ["data_folder"] or "./data/"

def get_data_file_with_suffix(user: str, suf: str):
    return os.path.join(DATA_FOLDER, f"{user}{suf}")

def get_users_from_file(filename: str):
    with open(path, 'r') as f:
        users = f.readlines()
    users = list( filter(lambda x: x, map(lambda x: x.strip(), users)) )
    return users 

result = {}

for username in sys.argv[1:]:
    user_dic = result[username] = result.get(username, {})
    for field in ['followers', 'followings']:
        path = get_data_file_with_suffix(username, f".{field}.txt")
        loaded_users = get_users_from_file(path)
        user_dic[field] = loaded_users

print(json.dumps(result))
