
def ord(a, p):
    o = 1;
    at = a;

    while at != 1:
        at = (a*at) % p
        o += 1

    return o

print(ord(5, 47))

