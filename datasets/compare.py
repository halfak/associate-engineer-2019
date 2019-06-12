import json
import sys

a = open(sys.argv[1])
b = open(sys.argv[2])

i = 0
for a_line, b_line in zip(a, b):
    i += 1
    a_doc = json.loads(a_line)
    b_doc = json.loads(b_line)

    assert a_doc == b_doc

assert i == 4677
