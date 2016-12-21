
Python script to remove least commonly used words from a document
Tested with Python3

Usage:
```
$ python3 truncate_file.py -i 74-0.txt -o 74-0-truncated.txt -d 35
```

74-0-truncated.txt is the output with 35% of least commonly used words in the document removed. The original file is 427479 bytes and the new file is 330396 bytes.
```
$ ls -lrt
total 756
-rw-rw-r-- 1 airbendr airbendr 427479 Dec 20 22:43 74-0.txt
-rw-rw-r-- 1 airbendr airbendr 330396 Dec 21 21:47 74-0-truncated.txt
```

