import numpy as np
import random

from generalized_random_response import GRR

class PEM():
    def __init__(self, sampleSet, domain):
        self.sampleSet = sampleSet
        self.domain = domain
        self.sampleSetBinary = np.copy(sampleSet)
        self.m = self.getM(domain)
        self.y = 
        self.orig_n =
        self.n = self.orig_n

        for i in range(len(self.sampleSetBinary)):
            self.sampleSetBinary[i] = self.intToBinaryString(self.sampleSetBinary[i])

        self.g = math.ceil((self.m - self.y) / self.n)
        self.G = [int(self.g)], []
        #for array in self.G:
        #    array.append()

        self.putIntoGroups()
        print(self.G)
        self.prefixes = [], []
        self.reportPrefixes();
        #print(self.prefixes[len(self.prefixes) - 1])

    def reportPrefixes(self):
        for i in range(int(self.g)):
            temp = []
            for j in range(len(self.G[i])):
                tempPrefix = intToBinaryString(self.G[i][j])[0:self.n]
                if (not i == 0):
                    for k in range(len(self.prefixes[i - 1])):
                        if (tempPrefix[0:self.n - self.orig_n] == self.prefixes[i - 1][k]):
                            temp.append(tempPrefix)
            tempGRR = GRR(20, (self.y + ((i + 1) * self.orig_n)), temp)
            perturbedGRR = tempGRR.perturbed
            for num in perturbedGRR:
                num = intToBinaryString(num)
            print(perturbed)
            self.prefixes.append(perturbedGRR)
            self.n += self.orig_n


    def putIntoGroups(self):
        for sample in self.sampleSet:
            rand = random.random();
            self.G[int(rand * self.g)].append(sample);

    def intToBinaryString(self, num):
        return (bin(int(num))[2:].zfill(self.domain))

    def getM(self, domain):
        return len("{0:b}".format(domain))
