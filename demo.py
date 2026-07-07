"""
demo.py
-------
Day 6 — Probability Distributions Demo

Runs all four visualisations in sequence.
Each plot opens in a separate window — close it to see the next one.

Usage:
    python demo.py
"""

from src.distribution import Gaussian, Poisson, Binomial, Bernoulli, Exponential
from src.visualizer import (
    plot_distribution_gallery,
    plot_parameter_sensitivity,
    plot_sample_convergence,
    plot_cdf,
)


def main():

    print("Plot 1/4 — Distribution Gallery")
    print("Shows PDF/PMF for all five distributions.")
    plot_distribution_gallery()

    print("Plot 2/4 — Parameter Sensitivity: Gaussian")
    print("Shows how sigma controls the spread of the bell curve.")
    plot_parameter_sensitivity(
        Gaussian,
        [
            {"mu": 0, "sigma": 0.5},
            {"mu": 0, "sigma": 1.0},
            {"mu": 0, "sigma": 2.0},
        ],
        x_range=(-6, 6),
    )

    print("Plot 3/4 — Parameter Sensitivity: Poisson")
    print("Shows how lambda controls the rate of events.")
    plot_parameter_sensitivity(
        Poisson,
        [
            {"lam": 1},
            {"lam": 3},
            {"lam": 7},
        ],
        x_range=(0, 20),
    )

    print("Plot 4/4 — Sample Convergence (Law of Large Numbers)")
    print("Shows sample mean converging to theoretical mean as n grows.")
    plot_sample_convergence(
        Gaussian(mu=5, sigma=2),
        ns=[10, 50, 100, 500, 1000, 5000, 10000],
    )

    print("Plot 5/5 — CDF Comparison")
    print("Compares cumulative distributions across different distributions.")
    plot_cdf(
        {
            "Gaussian(0, 1)": Gaussian(mu=0, sigma=1),
            "Gaussian(0, 2)": Gaussian(mu=0, sigma=2),
            "Exponential(1)": Exponential(lam=1),
            "Exponential(0.5)": Exponential(lam=0.5),
        },
        x_range=(-4, 6),
    )

    print("Done.")


if __name__ == "__main__":
    main()
