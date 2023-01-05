def get_middle(s):
    center = len(s) // 2
    if len(s) % 2 == 0:
        return s[(center - 1):(center + 1)]
    else:
        return s[center]


print(get_middle('String'))
print(get_middle('test'))
print(get_middle("testing"))
