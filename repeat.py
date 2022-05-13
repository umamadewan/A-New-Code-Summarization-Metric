ignore_list = ['the', 'an', 'a', 'is', 'are', 'have', 'has', 'of', 'on', 'in']


def is_repetition(text):
    words = text.split(" ")
    temp_words = words.copy()
    for item in temp_words:
        if item in ignore_list:
            words.remove(item)

    duplicate = list(set(words))

    if len(duplicate) < len(words):
        return -1
    return 3
