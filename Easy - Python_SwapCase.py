def swap_case(s):
    l = []
    for char in s:
        if char.isupper():
            l.append(char.lower())
        else:
            l.append(char.upper())
    return ''.join(l)