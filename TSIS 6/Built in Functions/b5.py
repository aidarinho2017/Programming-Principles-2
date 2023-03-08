def all_true(tup):
    return all(tup)
a = (True, True, True)
b = (True, True, True, False)
print(all_true(a))
print(all_true(b))