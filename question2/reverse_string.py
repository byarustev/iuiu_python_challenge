
def reverse_string(string):
    reversed_list = reversed(string)
    return "".join(reversed_list)


def recursion_reverse(string):
    if len(string) == 1:
        return string
    if len(string) < 0:
        return
    return string[-1] + recursion_reverse(string[:-1])


def reverse_using_list(string):
    our_list = list(string)
    our_list.reverse()
    return "".join(our_list)


# from first method
print(reverse_string("hello"))
print(reverse_string("world"))


# from second method
print(recursion_reverse("hello"))
print(recursion_reverse("world"))

# from third method
print(reverse_using_list("hello"))
print(reverse_using_list("world"))