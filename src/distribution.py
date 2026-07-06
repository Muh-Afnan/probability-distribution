import random
import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class Binomial:
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.q = 1 - p

    def PMF(self, X):
        pmf = (
            (factorial(self.n) / (factorial(X) * factorial(self.n - X)))
            * (self.p**X)
            * (self.q ** (self.n - X))
        )
        return pmf

    def PDF(self, X):
        raise NotImplementedError("PDF is not defined for discrete distributions.")

    def CDF(self, X):
        if X < 0:
            return 0
        return sum(self.PMF(k) for k in range(int(X) + 1))

    def sample(self, n_samples):
        results = []
        for _ in range(n_samples):
            successes = sum(1 for _ in range(self.n) if random.random() < self.p)
            results.append(successes)
        return results

    def mean(self):
        return self.n * self.p

    def variance(self):
        return self.n * self.p * self.q

    def std(self):
        return (self.variance()) ** 0.5


class Bernoulli:
    def __init__(self, p):
        self.p = p
        self.q = 1 - p

    def PMF(self, X):
        if X == 1:
            return self.p
        elif X == 0:
            return self.q
        else:
            return 0

    def PDF(self, X):
        raise NotImplementedError("PDF is not defined for discrete distributions.")

    def CDF(self, X):
        if X < 0:
            return 0
        elif X < 1:
            return self.q
        elif X == 1:
            return 1
        else:
            return 1

    def sample(self, n_samples):
        samples = []
        for _ in range(n_samples):
            rand_num = random.random()
            if rand_num < self.p:
                samples.append(1)
            else:
                samples.append(0)
        return samples

    def mean(self):
        return self.p

    def variance(self):
        return self.p * self.q

    def std(self):
        return (self.variance()) ** 0.5


class Gaussian:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def mean(self):
        return self.mu

    def variance(self):
        return self.sigma**2

    def std(self):
        return self.sigma

    def PMF(self, X):
        raise NotImplementedError("PMF is not defined for continuous distributions.")

    def PDF(self, X):
        coefficient = 1 / (self.sigma * math.sqrt(2 * math.pi))
        exponent = math.exp(-0.5 * ((X - self.mu) / self.sigma) ** 2)
        return coefficient * exponent

    def sample(self, n_samples):
        samples = []
        for _ in range(n_samples):
            u1 = random.random()
            u2 = random.random()
            z = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
            samples.append(z * self.sigma + self.mu)
        return samples

    def CDF(self, X):
        return 0.5 * (1 + math.erf((X - self.mu) / (self.sigma * (2**0.5))))


class Poisson:
    def __init__(self, lam):
        self.lam = lam

    def PMF(self, K):
        pmf = math.exp(-self.lam) * (self.lam**K) / factorial(K)
        return pmf

    def PDF(self, X):
        raise NotImplementedError("PDF is not defined for discrete distributions.")

    def mean(self):
        return self.lam

    def variance(self):
        return self.lam

    def std(self):
        return (self.variance()) ** 0.5

    def CDF(self, K):
        if K < 0:
            return 0
        else:
            return sum(self.PMF(k) for k in range(K + 1))

    def sample(self, n_samples):
        samples = []
        for _ in range(n_samples):
            L = math.exp(-self.lam)
            k = 0
            p = 1
            while p > L:
                k += 1
                p *= random.random()
            samples.append(k - 1)
        return samples


class Exponential:
    def __init__(self, lam):
        self.lam = lam

    def PMF(self, X):
        raise NotImplementedError("PMF is not defined for continous distributions.")

    def PDF(self, X):
        if X >= 0:
            return self.lam * math.exp(-self.lam * X)

    def mean(self):
        return 1 / self.lam

    def variance(self):
        return 1 / (self.lam**2)

    def std(self):
        return (self.variance()) ** 0.5

    def CDF(self, X):
        return 1 - math.exp(-self.lam * X) if X >= 0 else 0

    def sample(self, n_samples):
        samples = []
        for _ in range(n_samples):
            samples.append(-math.log(random.random()) / self.lam)
        return samples
