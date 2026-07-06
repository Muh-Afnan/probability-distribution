import unittest
import math
from src.distribution import Bernoulli, Binomial, Gaussian, Poisson, Exponential


class TestDistributions(unittest.TestCase):

    # Bernoulli
    def test_bernoulli_pmf_sums_to_one(self):
        b = Bernoulli(0.7)
        self.assertAlmostEqual(b.PMF(0) + b.PMF(1), 1.0)

    def test_bernoulli_cdf_at_one_is_one(self):
        self.assertEqual(Bernoulli(0.3).CDF(1), 1.0)

    def test_bernoulli_sample_only_zero_or_one(self):
        samples = Bernoulli(0.5).sample(1000)
        self.assertTrue(all(s in [0, 1] for s in samples))

    # Binomial
    def test_binomial_pmf_sums_to_one(self):
        b = Binomial(0.3, 10)
        total = sum(b.PMF(k) for k in range(11))
        self.assertAlmostEqual(total, 1.0, places=5)

    def test_binomial_mean(self):
        b = Binomial(0.4, 20)
        self.assertAlmostEqual(b.mean(), 8.0)

    # Gaussian
    def test_gaussian_pdf_peak_at_mean(self):
        g = Gaussian(0, 1)
        self.assertGreater(g.PDF(0), g.PDF(1))

    def test_gaussian_cdf_at_mean_is_half(self):
        self.assertAlmostEqual(Gaussian(5, 2).CDF(5), 0.5, places=5)

    def test_gaussian_sample_mean_converges(self):
        g = Gaussian(10, 2)
        samples = g.sample(10000)
        self.assertAlmostEqual(sum(samples) / len(samples), 10, delta=0.1)

    # Poisson
    def test_poisson_pmf_sums_to_one(self):
        p = Poisson(3)
        total = sum(p.PMF(k) for k in range(50))
        self.assertAlmostEqual(total, 1.0, places=4)

    def test_poisson_mean(self):
        self.assertEqual(Poisson(5).mean(), 5)

    # Exponential
    def test_exponential_cdf_approaches_one(self):
        e = Exponential(1)
        self.assertAlmostEqual(e.CDF(100), 1.0, places=4)

    def test_exponential_sample_mean_converges(self):
        e = Exponential(2)
        samples = e.sample(10000)
        self.assertAlmostEqual(sum(samples) / len(samples), 0.5, delta=0.05)


if __name__ == "__main__":
    unittest.main()
