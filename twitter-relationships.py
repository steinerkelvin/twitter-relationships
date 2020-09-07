#!/usr/bin/env python3
# encoding: utf-8
import sys
import argparse
import json

FOLLOWER = '<-'
FOLLOWING = '->'

RELATIONS = [
    {FOLLOWER, FOLLOWING},
    {FOLLOWER},
    {FOLLOWING}
]

def relation_to_string(rel, reverse=False):
    d1 = FOLLOWER in rel
    d2 = FOLLOWING in rel
    if reverse:
        (d1, d2) = (d2, d1)
    s1 = "<" if d1 else "="
    s2 = ">" if d2 else "="
    return f"{s1}=={s2}"

# Returns true if all items in `items` are also in `col`,
# otherwise, returns false
def all_in(items):
    def f(col):
        for item in items:
            if not item in col:
                return False
        return True
    return f

def reverse(txt: str):
    return txt[::-1]

parser = argparse.ArgumentParser()
parser.add_argument('user1', type=str)
parser.add_argument('user2', type=str)

args = parser.parse_args()
data = json.load(sys.stdin)

all_users = {}

tgtuser1, tgtuser2 = tgtusers = [args.user1, args.user2]

for tgtuser in tgtusers:
    for follower in data[tgtuser]['followers']:
        all_users.setdefault(follower, {})
        all_users[follower].setdefault(tgtuser, set())
        all_users[follower][tgtuser].add(FOLLOWER)
    for following in data[tgtuser]['followings']:
        all_users.setdefault(following, {})
        all_users[following].setdefault(tgtuser, set())
        all_users[following][tgtuser].add(FOLLOWING)

common_users = { 
    user: value
        for (user,value) in all_users.items()
        if all_in(tgtusers)(value.keys())
}

# from pprint import pprint
# pprint(common_users)

for r1 in RELATIONS:
    for r2 in RELATIONS:
        group_users = []
        for (user, value) in common_users.items():
            if value[tgtuser1] == r1 and value[tgtuser2] == r2:
                group_users.append(user)
        if not group_users:
            continue

        rels1 = relation_to_string(r1)
        rels2 = relation_to_string(r2, reverse=True)
        print(f"{tgtuser1} {rels1} X {rels2} {tgtuser2}")
        for user in group_users:
            print(user)
        print()
