#!/usr/bin/env python3
#uniquewords2.py 
#same as uniquewords1.py but adds default dictionary

import collections
import string
import sys


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
for word in sorted(words):
    print("{0} occurs {1} times".format(word, words[word]))
