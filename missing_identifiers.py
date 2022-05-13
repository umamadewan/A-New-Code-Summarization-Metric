from re import search
nouns_list = ['_NN', '_NNS', '_NNP', '_NNPS']


def return_nouns(text):
    words = text.split(" ")
    temp_words = words.copy()
    returned_nouns = []
    for item in temp_words:
        for noun in nouns_list:
            if search(noun, item.strip().upper()):
                returned_nouns.append(item.split("_")[0])
                break
    return returned_nouns


def check_missing_identifiers(human, model):
    if len(model) == 0:
        return -2
    for noun in human:
        if noun not in model:
            return -1

    return 5
