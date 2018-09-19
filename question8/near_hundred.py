def near_100(x, y):

    if x != y:
        x1 = int(round(x - 100))
        y1 = int(round(y - 100))

        if x1 < y1:
            return x
        if y1 < x1:
            return y

    else:
        return False


print(near_100(90, 89))
print(near_100(-90, -89))
print(near_100(90, 90))

# you can input other numbers to test this
