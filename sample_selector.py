#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import numpy as np

class SampleSelector:

    def __init__(self, sampleSize, domain):
        self.sampleSize = sampleSize
        self.domain = domain
        self.sampleSet = np.zeros(self.sampleSize)
        self.getNewSampleSet();

    def getNewSampleSet(self):
        for i in range(self.sampleSize):
            self.sampleSet[i] = random.randint(0, self.domain)
