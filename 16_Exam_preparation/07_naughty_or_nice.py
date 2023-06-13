def naughty_or_nice_list(lst, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []

    found_match = []

    for arg in args:
        parts = arg.split("-")
        number = parts[0]
        word = parts[1]
        if word == "Naughty":
            for item in lst:
                if item[0] == int(number):
                    found_match.append(item)
            if len(found_match) == 1:
                naughty.extend(found_match)
                lst.remove(found_match[0])
            found_match = []

        elif word == "Nice":
            for item in lst:
                if item[0] == int(number):
                    found_match.append(item)
            if len(found_match) == 1:
                nice.extend(found_match)
                lst.remove(found_match[0])
            found_match = []

    for name, value in kwargs.items():
        for item in lst:
            if item[1] == name:
                found_match.append(item)
        if len(found_match) == 1:
            if value == "Naughty":
                naughty.append(found_match[0])
                lst.remove(found_match[0])
            elif value == "Nice":
                nice.append(found_match[0])
                lst.remove(found_match[0])

        found_match = []

    not_found.extend(lst)

    result = ""
    if nice:
        result += "Nice: " + ", ".join(name for _, name in nice) + "\n"
    if naughty:
        result += "Naughty: " + ", ".join(name for _, name in naughty) + "\n"
    if not_found:
        result += "Not found: " + ", ".join(name for _, name in not_found) + "\n"

    return result


# print(naughty_or_nice_list(
#     [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

print(naughty_or_nice_list(
    [(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ],
    "3-Nice", "5-Naughty", "2-Nice", "1-Nice",
))