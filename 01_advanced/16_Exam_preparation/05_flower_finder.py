from collections import deque


def check_word(letter, word):
    if letter in word:
        word = word.replace(letter, "")
    return word


vowels = deque(input().split())
consonants = deque(input().split())

given_words = ["rose", "tulip", "lotus", "daffodil"]

found_word = False


while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for index in range(len(given_words)):
        given_words[index] = check_word(vowel, given_words[index])
        if given_words[index] == "":
            found_word = True
            break

        given_words[index] = check_word(consonant, given_words[index])
        if given_words[index] == "":
            found_word = True
            break
    if found_word:
        break

if found_word:
    if given_words[0] == "":
        print("Word found: rose")
    elif given_words[1] == "":
        print("Word found: tulip")
    elif given_words[2] == "":
        print("Word found: lotus")
    elif given_words[3] == "":
        print("Word found: daffodil")
else:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")



