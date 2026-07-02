from collections import Counter
from random import Random

class Distribution:
    def __init__(self, data: list["int | float"]):
        self.data = data

    def pmf(self, k):
        n = len(self.data)
        count = Counter(k for k in self.data)
        return count.get(k, 0) / n if n > 0 else 0

    def pdf(self, x):
        pass

    def cdf(self, x):
        pass

    def sample(self, n):
        mean = self.mean()
        std = self.std()
        samples = []
        rng = Random()
        for _ in range(n):
            sample = mean + std * (2 * rng.random() - 1)
            samples.append(sample)
        return samples


    def mean(self):
        return sum(self.data) / len(self.data)

    def variance(self):
        mu = self.mean()
        var = sum([(x - mu) ** 2 for x in self.data]) / len(self.data)
        return var

    def std(self):
        return self.variance() ** 0.5
