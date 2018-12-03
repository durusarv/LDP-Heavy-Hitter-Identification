#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import nltk
nltk.download('brown')
from nltk.corpus import brown

def main():
    sampleSet = setOfSamples(5, 5)
    for sampSet in sampleSet:
        print(sampSet)
    return 0

def setOfSamples(sampleSize, numOfSamples):
    sampleSet = []
    i = 0
    while (i < numOfSamples):
        sampleSet.append(sampleData(sampleSize))
        i += 1
    return sampleSet

def sampleData(sampleSize):
    sampleSet = []
    words = brown.words()
    i = 0
    while (i < sampleSize):
        rand = random.randint(0,len(words))
        randWord = words[rand].lower()
        while (not randWord[0].isalpha() and len(randWord) == 1):
            rand = random.randint(0,len(words))
            randWord = words[rand].lower()
        sampleSet.append(randWord)
        i += 1
        
    return sampleSet

if __name__ == "__main__":
    main()