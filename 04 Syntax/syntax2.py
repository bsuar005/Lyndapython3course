#!/usr/bin/python3
# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

from    pprint import pprint

def main():
    func(1)


def func(a):
    for i in range(a, 10):
        pprint(i)

if __name__ == "__main__": main()
