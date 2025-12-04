import itertools
f = open("test.dat", "r")

total = 0
l = 0
for i in f:
    pairs = []
    line = list(i.rstrip())
    for x in itertools.combinations(line,2):
        pairs.append(''.join(x))
    total += int(max(pairs))
    l += 1
print("Part 1 = ", total)

f.seek(0)
for i in f:
    line_length = (len(i))

    # If we have a 9 at least 12 away from the end, we can chop everything before it
    print(i.index(max(i)))
