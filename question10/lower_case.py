def upper_lower(string):
    if len(string) < 3:
        return string.upper()

    front_part = string[0:3].lower()
    back_part = string[3:len(string)].upper()
    return front_part + back_part


print(upper_lower("Python"))
print(upper_lower("Py"))
print(upper_lower("JAVAScript"))
