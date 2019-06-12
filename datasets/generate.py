import json
import random

import requests

response = requests.get(
    "https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt")
names = [n.strip() for n in response.text.split("\n")]
names_i = list(range(0, len(names)))

a = open("a.json", "w")
b = open("b.json", "w")

a_simple = open("a.simple.json")
b_simple = open("b.simple.json")

a_next = json.loads(next(a_simple))
b_next = json.loads(next(b_simple))
i = 0
while a_next or b_next:
    if a_next and b_next and a_next['rev_id'] == b_next['rev_id']:
        a_id = random.choice(names_i)
        if i % 7 == 0:
            b_id = a_id+1
        else:
            b_id = a_id

        if i % 23 != 0:
            a_next['user'] = {'id': a_id, 'name': names[a_id]}

        b_next['user'] = {'id': b_id, 'name': names[b_id]}

        a.write(json.dumps(a_next))
        a.write("\n")
        b.write(json.dumps(b_next))
        b.write("\n")
        try:
            a_next = json.loads(next(a_simple))
        except StopIteration:
            a_next = None
        try:
            b_next = json.loads(next(b_simple))
        except StopIteration:
            b_next = None
    elif not b_next or a_next['rev_id'] < b_next['rev_id']:
        a_id = random.choice(names_i)
        a_next['user'] = {'id': a_id, 'name': names[a_id]}
        a.write(json.dumps(a_next))
        a.write("\n")
        try:
            a_next = json.loads(next(a_simple))
        except StopIteration:
            a_next = None
    else:  # not a_next or b_next['rev_id'] < a_next['rev_id']
        b_id = random.choice(names_i)
        b_next['user'] = {'id': b_id, 'name': names[b_id]}
        b.write(json.dumps(b_next))
        b.write("\n")
        try:
            b_next = json.loads(next(b_simple))
        except StopIteration:
            b_next = None
    i += 1
