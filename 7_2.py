d = {}
with open("students.csv") as f:
    next(f)
    for line in f:
        h, nm, a, db = line.split(";")
        d.setdefault(int(h), []).append((nm, int(a), db))
l = d.values()
l = list(l)
l.sort()
print(l)

