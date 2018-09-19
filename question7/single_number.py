def return_single(nums_list):
    for i in nums_list:
            if nums_list.count(i) == 1:
                return i
    return None


print(return_single([5, 3, 4, 3, 5, 5, 3]))