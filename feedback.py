#!/usr/bin/env python2.7
# -*- encoding: utf-8 -*-

import sys
import argparse
import random


data = {}

patterns = ["intro action prop", "intro2 prop2", "addon addon-prop", "addon2"]

f = open("data.txt")
for l in f:
    t = l.rstrip("\r\n").decode("utf-8").split("\t")
    if t[0] not in data:
        data[t[0]] = []
    data[t[0]].append(t[1])
f.close()

def add_pattern(prev, pattern=None):
    res = prev.strip(" .") + "."
    words = set(res.replace(".", " ").split(" "))
    if pattern is None:
        pattern = random.choice(patterns)
    for part in pattern.split(" "):
        ad = random.choice(data[part])
        wordsad = set(ad.replace(".", " ").split(" "))
        if len(words & wordsad) > 3:
            ad = random.choice(data[part])
        res += " " + ad

    res = res.strip(" .") + "."
    return res

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python feedback.py <USERNAME@>"
        exit(1)

    res = ""
    res = add_pattern(res, random.choice(patterns[0:1]))
    for i in range(0, random.randint(1, 4)):
        res = add_pattern(res, patterns[3])
    res = add_pattern(res, patterns[2])

    print res.replace("%1", sys.argv[1].decode("utf-8")).encode("utf-8")
