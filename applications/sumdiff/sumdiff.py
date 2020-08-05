"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def cmp(a, b, c, d):
    """eval the statment (a + b) == (c - d) and return true or false"""
    cond = (a + b) == (c - d)
    print(f"f({a}) + f({b}) == f({c}) - f({d}) is {cond}")
    return cond


# Your code here
print("starting list: ")
print(q)

print("f(x) computed function table")
table = {k: f(k) for k in q}
print(table)

out = []

row_ind = 0

while row_ind < len(table):

    # assign vars from the function table
    try:
        a = table[q[row_ind]]
        b = table[q[row_ind + 1]]
        c = table[q[row_ind + 2]]
        d = table[q[row_ind + 3]]

        if cmp(a, b, c, d):
            out.append([a, b, c, d])
        else:
            row_ind += 1

        # exit condition
        if row_ind == len(table) - 4:
            break

    except Exception as e:
        print("ERROR:\n", e)
        print("CURRENT VALUE OF TABLE:\n", table)
        print("LAST row_ind:", row_ind)

print(out)
