import random

def check(x):
    for item in range(len(x) - 1):
        if x[item] > x[item + 1]:
            return True

    else:
        return False

def bogosort(x):
    while check(x):
        random.shuffle(x)

    return x
