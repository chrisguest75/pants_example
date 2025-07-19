from dictionary import Dictionary

def main():
    dictionary = Dictionary()
    dictionary.load_words_from_file('./words_alpha.txt')

    words = dictionary.complete_word("abuse")
    #for word in words:
    #    print(word)

    lengths = [{'word': x, 'length':len(x)} for x in words]
    sorted_lengths = sorted(lengths, key=lambda x: x['length'])
    for word in sorted_lengths:
        print(word['word'])


if __name__ == "__main__":
    main()
