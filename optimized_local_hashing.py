# -*- coding: utf-8 -*-
"""
@author: durusarv, jdlips, tycorr (Duruvan Sarvanan, Jake Lipson and Tyler Correll)
"""

import numpy as np
import xxhash
import math

class OLH:

    def __init__(self, epsilon, domain, data):

        self.d = domain
        self.epsilon = epsilon
        self.p = math.exp(self.epsilon) / (math.exp(self.epsilon) + self.d - 1)

        self.numUsers = len(data)
        self.perturbed = np.zeros(self.numUsers)

        self.estimate = np.zeros(self.numUsers)

        self.randomIdxs = np.random.rand(1, self.numUsers)

        self.pi()
        self.aggregator()

    def pi(self):

        for i in range(self.numUsers):

            hashed = (xxhash.xxh32(str(self.randomIdxs[0][i]), seed=i).intdigest() % (math.exp(self.epsilon) + 1))

            if np.random.random_sample() > self.p:
                sample = np.random.randint(0, math.exp(self.epsilon) - 1)
                if sample >= hashed:
                    sample += 1
                self.perturbed[i] = sample
            else:
                self.perturbed[i] = hashed

    def aggregator(self):

        for i in range(self.numUsers):
            for j in range(self.d):
                if self.perturbed[i] == (xxhash.xxh32(str(self.randomIdxs[0][i]), seed=i).intdigest() % (math.exp(self.epsilon) + 1)):
                    self.estimate[j] += 1
        x = math.exp(self.epsilon) + 1 / (self.p * (math.exp(self.epsilon)) - 1)
        y = (1.0 * self.numUsers) / (self.p * math.exp(self.epsilon) - 1)
        self.estimate = x * self.estimate - y
