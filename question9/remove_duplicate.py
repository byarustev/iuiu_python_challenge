def remove_duplicates(string):
    old_string_list = string.split(" ")
    new_string_list = [old_string_list[0]]

    for word in old_string_list[1:]:
        if word in new_string_list:
            pass
        else:
            new_string_list.append(word)

    return " ".join(new_string_list)


print(remove_duplicates("The boy boy is going to school school"))