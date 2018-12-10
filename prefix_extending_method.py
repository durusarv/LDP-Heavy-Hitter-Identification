import numpy as np
               
class PEM():
    def __init__(self, sampleSet, domain):
        self.sampleset = sampleSet
        self.domain = domain
        self.sampleSetBinary = np.copy(sampleSet)

        for i in range(len(self.sampleSetBinary)):
            sampleSetBinary[i] = intToBinaryString(sampleSetBinary[i], self.domain)

def intToBinaryString(num, domain):
    length = len("{0:b}".format(domain))
    return bin(num)[2:].zfill(length)
