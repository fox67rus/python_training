# merge dictionary
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4 }
d2 = {'e': 5, 'f': 6, 'g': 7}

# 1
print({**d1, **d2})
#2
print(dict(d1.items() | d2.items()))
#3
d1.update(d2)
print(d1)


