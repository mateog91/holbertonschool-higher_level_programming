def complex_delete(a_dictionary, value):
    toDelet = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            toDelet.append(key)

    for key in toDelet:
        del a_dictionary[key]

    return a_dictionary
