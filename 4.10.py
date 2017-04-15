#iterating Over the Index-Value Pairs of a Sequence
>>> my_list = ['a', 'b', 'c']
>>> for idx, val in enumerate(my_list):
...     print(idx, val)
...
0 a
1 b
2 c

>>> my_list = ['a', 'b', 'c']
>>> for idx, val in enumerate(my_list, 1):    #The enumerate object yields pairs containing a count (from start)
...     print(idx, val)
...
1 a
2 b
3 c


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
                ...
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))




word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()
#now we get a list
for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)


data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# Correct!
for n, (x, y) in enumerate(data):