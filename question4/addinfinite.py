def sum(*args):
    total_sum = 0
    for i in args:
        total_sum += i

    return total_sum


print(sum(1,2,3,4,5))
print(sum(4,5))
print(sum(5))

