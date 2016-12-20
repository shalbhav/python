# Script to create all possible anagrams from a given word and
# check with a dictionary file for english words from the list.
# Tested with Python3

from itertools import permutations

if __name__=="__main__":
    inword = input("Enter word : ")
    # permute the word
    perms = [''.join(p) for p in permutations(inword)]
    print("{} combinations of words from {}\n".format(len(perms), inword))

    enwords_file = input("Enter path to dictionary file : ")
    with open(enwords_file) as f:
        english_words = set(word.strip().lower() for word in f)

    w = set(w for w in perms if w.lower() in english_words)
    if w:
        print("List of possible words:\n", w)
    else:
        print("No words found\n")

