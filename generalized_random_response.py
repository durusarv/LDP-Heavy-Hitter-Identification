# -*- coding: utf-8 -*-
"""
@author: durusarv, jdlips, tycorr (Duruvan Sarvanan, Jake Lipson and Tyler Correll)
"""

import numpy as np
import xxhash
import math

class GRR:

    def __init__(self, epsilon, domain, data):

        self.data = data
        self.d = domain
        self.epsilon = epsilon
        self.p = math.exp(self.epsilon) / (math.exp(self.epsilon) + self.d - 1)

        self.estimate = np.zeros(self.d)

        self.numUsers = len(data)
        self.perturbed = np.zeros(self.numUsers)

        self.q = 1 / (math.exp(self.epsilon) + self.d - 1)

        self.pi()
        self.aggregator()

    def pi(self):
        for i in range(self.numUsers):
            coin = np.random.random()
            if coin <= self.p:
                self.perturbed[i] = self.data[i]
            else:
                temp = np.random.randint(0, len(self.data) - 1)
                if (temp == i):
                    temp += 1
                self.perturbed[i] = self.data[temp]

    def aggregator(self):
        for i in range(self.numUsers):
            for j in range(self.numUsers):
                if self.perturbed[i] == self.perturbed[j]:
                    self.estimate[i] += 1
        for i in range(self.estimate):
            self.estimate[i] = (self.estimate[i] - (self.numUsers * self.q)) / (self.p - self.q)
