# -*- coding: utf-8 -*-
"""
@author: durusarv, jdlips, tycorr (Duruvan Sarvanan, Jake Lipson and Tyler Correll)
"""

import numpy as np
import xxhash
import math

class GRR:

    def __init__(self, dist, epsilon, domain, data):

        self.d = domain
        self.epsilon = epsilon
        self.p = math.exp(self.epsilon) / (math.exp(self.epsilon) + self.d - 1)

        self.real = dist
        self.estimate = np.zeros(self.d)

        self.numUsers = len(data)
        self.perturbed = np.zeros(self.numUsers)

        self.q = 1 / (math.exp(eps) + d - 1)
        #self.randomIdxs = np.random.rand(1, self.numUsers)

    def pi(self):
        for i in range(self.numUsers):
            coin = np.random.random()
            if coin <= self.p:
                self.pertubed[i] = data[i]
            else:
                temp = np.random.randint(0, len(data) - 1
                if (temp == i):
                    temp += 1
                self.pertubed[i] = data[temp]

    def aggregator(self):
        for i in range(self.numUsers):
            for j in range(self.d):
                if pertubed[i] == self.d[j]:
                    self.estimate[j] += 1
        for i in range(self.estimate):
            self.estimate[i] = (self.estimate[i] - (self.numUsers * self.q)) / (self.p - self.q)
