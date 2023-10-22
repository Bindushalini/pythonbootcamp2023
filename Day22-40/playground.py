def add(*args):
    sum = 0
    for _ in args:
        sum += _
    return sum


print(add(3, 5, 2, 1))

def some_operation(**kwargs):
    total = 0
    total += kwargs["sum"]
    total *= kwargs["mult"]
    print(total)

some_operation(sum=2,mult=9)