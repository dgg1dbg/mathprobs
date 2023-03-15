x, y, p = [int(x) for x in input().split()]

def modulaofpower(x, y, p):
    res = 1
    x = x % p

    while y > 0:
        if y % 2 != 0:
            res = (res * x) % p
            y -= 1
        
        y /= 2
        x = (x * x) % p
    
    return res

print(modulaofpower(x, y, p))
