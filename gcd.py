def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
    
a, b = [int(x) for x in input().split()]
print(gcd(a, b))