def get_word_counts(filename):
    my_file = open(filename)

    word_counts = {}

    for line in my_file:
        words = line.split()
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_count_for_word(word_counts):
    # return word_counts.get(word, 0)

    # counts = get_word_counts(' ')
    # print (get_count_for_word(counts, 0))
    # for key in word_counts:
    #     print key, word_counts[key]

    for key, value in word_counts.items():
        print key, value


word_tally = get_word_counts("test.txt")
get_count_for_word(word_tally)