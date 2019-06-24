# Associate Engineer Task

This project contains code and instructions for completing the Wikimedia Foundation's
task for the Associate Software Engineer position (see the job description).

To complete the task, read the following problem description and implement a solution.
Please submit your solution (the code and a one-page description how you approached this
problem and why) to ahalfaker@wikimedia.org.

# The Problem

A researcher on the machine learning team needs you to implement a *python utility* for
processing training datasets.  For various reasons, we have different datasets that
need to be merged based on a matching identifier ("rev_id").  Data file
contains lines of JSON blobs.  E.g.,
```
{"rev_id": 1001, "damaging": false, "goodfaith": true}
{"rev_id": 1002, "damaging": true, "goodfaith": false}
```

The JSON blobs are ordered by "rev_id" in increasing order.

# The Task
Write a python utility called "union_merge.py" that recursively merges
together the fields that are present in each file and prints out JSON lines with
merged information.  All rows should be returned whether they have a corresponding
matching line in the other file or not.  When both files contain the same field,
preference should be given to the fields in the second file ("b.json").  Output 
should also be in sorted order.

## An example:

File "a.json":
```
{"rev_id": 1000, "damaging": true, "goodfaith": false}
{"rev_id": 1001, "damaging": false, "goodfaith": true, "user": {"id": 101}}
{"rev_id": 1002, "damaging": true, "goodfaith": false, "user": {"id": 0}}
```

File "b.json":
```
{"rev_id": 999, "damaging": true, "goodfaith": false, "user": {"id": 100, "name": "Sam"}}
{"rev_id": 1001, "user": {"name": "Amir"}}
{"rev_id": 1002, "damaging": true, "goodfaith": true, "user": {"id": 102, "name": "Pete"}}
```

A call to `python union_merge.py a.json b.json` should print:
```
{"rev_id": 999, "damaging": true, "goodfaith": false, "user": {"id": 100, "name": "Sam"}}
{"rev_id": 1000, "damaging": true, "goodfaith": false}
{"rev_id": 1001, "damaging": false, "goodfaith": true, "user": {"id": 101, "name": "Amir"}}
{"rev_id": 1002, "damaging": true, "goodfaith": true, "user": {"id": 102, "name": "Pete"}}
```

# Your solution

Your solution should contain an implementation of `union_merge.py`, a `README.md` containing
your writeup, and a file called "output.json" that contains the result of a run of
`python union_merge.py a.json b.json` from this repository.

In your writeup about this problem, describe your approach to your solution and why you
chose it.  Also answer the following questions:

1. What python data structures did you make use of and why?
2. What would happen if `a.json` and `b.json` were too big to fit into memory?
3. Would your solution still work if `a.json` and `b.json` were not sorted by "rev_id"?
4. How would you go about adding tests for your solution?
