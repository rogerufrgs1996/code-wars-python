string = "sTress"
def first_non_repeating_letter(string):
    lowercase = string.casefold()
    for x in lowercase:
        r = lowercase.count(x)
        if r == 1:
            return string[lowercase.find(x)]
    return ''


print(first_non_repeating_letter(string))
