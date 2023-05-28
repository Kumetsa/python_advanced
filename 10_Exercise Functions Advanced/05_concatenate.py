def concatenate(*args, **kwargs):
    text = ''.join(args)

    for key, val in kwargs.items():
        text = text.replace(key, val)

    return text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))


# {'UNI': 'Uni', 'Grate': 'Great'}
# {'C': 'P', 's': '', 'java': 'Java'}