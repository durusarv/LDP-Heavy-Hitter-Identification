from sample_selector import SampleSelector
from optimized_local_hashing import OLH
from generalized_random_response import GRR

def main():
    domain = 15
    epsilon = 1
    ss = SampleSelector(domain, 'news')
    sampleSet = ss.sampleSet

    grr = GRR(epsilon, domain, sampleSet)
    olh = OLH(epsilon, domain, sampleSet)

    grrEstimate = grr.estimate
    olhEstimate = olh.estimate

    print(sampleSet)
    print(grrEstimate)
    print(olhEstimate)

if __name__ == "__main__":
    main()
