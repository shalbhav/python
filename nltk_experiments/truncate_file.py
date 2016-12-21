# Python script to remove least commonly used words from a document
# Tested with Python3
import sys
import argparse
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

if __name__=="__main__":

    # append path to nltk_data files
    nltk.data.path.append('/path/to/nltk_data')

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ifile", help="input file", required=True)
    parser.add_argument("-o", "--ofile", help="output file", required=True)
    parser.add_argument("-d", "--del_percent",
                        help="percent (floating point number) of least common \
                        words to be deleted from INPUT file", required=True)
    args = parser.parse_args()

    in_file = args.ifile
    out_file = args.ofile
    del_percent = float(args.del_percent)

    with open(in_file, 'r') as inf:
        intxt = inf.read()

    words = word_tokenize(intxt)
    num_words = len(words)
    num_retain_words = int(num_words - (del_percent*num_words)/100.0)

    # Remove del_percent of words
    retain_words = Counter(words).most_common(num_retain_words)
    retain_words_dict = dict(retain_words)

    try:
        with open(in_file, 'r') as inf, open(out_file, 'w') as outf:
            for line in inf:
                # write out words only in retain_words_dict
                new_line = [w for w in line.split() if w in retain_words_dict]
                outf.write(" ".join(new_line))
                outf.write("\n")
    except IOError as e:
        print("Operation failed: {}".format(e.strerror))
