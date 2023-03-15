x, y, p = [int(x) for x in input().split()]

def recursivemodexp(x, y, p):
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            return (recursivemodexp(x, y//2, p) ** 2) % p
        else:
            return (((recursivemodexp(x, y//2, p) ** 2) % p) * x) % p

print(recursivemodexp(x, y, p))