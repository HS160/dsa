def fact(num):
    if num == 0:
        return 1
    if num == 1:
        return 1
    x = num * fact(num-1)
    return x

y = fact(5)
print(y)