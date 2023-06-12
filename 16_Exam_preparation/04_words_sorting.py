def words_sorting(*words):
    dict_of_words = {}
    total_value = 0
    formatted_output = ""
    for word in words:
        dict_of_words[word] = 0
        for el in word:
            dict_of_words[word] += ord(el)
            total_value += ord(el)
    if total_value % 2 == 0:
        sorted_words = sorted(dict_of_words.items(), key=lambda x: x[0], reverse=False)
    else:
        sorted_words = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)

    for word, value in sorted_words:
        formatted_output += f"{word} - {value}\n"

    return formatted_output


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))


