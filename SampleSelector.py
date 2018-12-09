#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import nltk
nltk.download('brown')
from nltk.corpus import brown

class SampleSelector:

def __init__(self, sampleSize, category):
    self.sampleSize = sampleSize
    self.category = category

    def getNewSampleSet(sampleSize, category):
        sampleSet = []
        words = brown.words(categories = self.category)
        i = 0
        while (i < self.sampleSize):
            rand = random.randint(0,len(words))
            randWord = words[rand].lower()
            while (not randWord[0].isalpha() and len(randWord) == 1):
                rand = random.randint(0,len(words))
                randWord = words[rand].lower()
            sampleSet.append(randWord)
            i += 1
        return sampleSet

    def setSampleSize(size):
        self.sampleSize = size;

    def setCategory(category):
        self.category = cat
