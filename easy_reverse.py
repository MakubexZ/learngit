# -*- coding: utf-8 -*-

def reverse(x):
    if x < -2147483648 or x >= 2147483648:
        return 0
    else:
        if x < 0:
            y = str(x)
            z = y
            y = y[::-1]
            y = y[:-1]
            y = int(y)
            y = -y
            if y < -2147483648 or y >= 2147483648:
                return 0
            else:
                return y
        else:
            y = str(x)
            y = y[::-1]
            print(y)
            y = int(y)
            print(y)
            if y < -2147483648 or y >= 2147483648:
                return 0
            else:
                return y
    #return y


h = reverse(1753497599)
m = h
print(m)
