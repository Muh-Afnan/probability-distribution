import math
import matplotlib.pyplot as plt
from src.distribution import Exponential, Gaussian, Poisson, Binomial, Bernoulli


def plot_distribution_gallery():
    """
    distributions = {
        "Gaussian(0,1)": gaussian_obj,
        "Poisson(3)": poisson_obj,
        ...
    }
    Plots PDF/PMF for each distribution in a grid.
    """

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))

    g = Gaussian(0, 1)
    x_values = [i * 0.1 for i in range(-400, 400)]
    y_values = [g.PDF(x) for x in x_values]
    ax = axes[0, 0]
    ax.plot(x_values, y_values)
    ax.set_title("Gaussian(0,1)")
    ax.set_xlabel("x")
    ax.set_ylabel("PDF")

    e = Exponential(1)
    x_values = [i * 0.1 for i in range(100)]
    y_values = [e.PDF(x) for x in x_values]
    ax = axes[0, 1]
    ax.plot(x_values, y_values)
    ax.set_title("Exponential(1)")
    ax.set_xlabel("x")
    ax.set_ylabel("PDF")

    p = Poisson(3)
    x_values = [i for i in range(15)]
    y_values = [p.PMF(x) for x in x_values]
    ax = axes[0, 2]
    ax.bar(x_values, y_values)
    ax.set_title("Poisson(3)")
    ax.set_xlabel("x")
    ax.set_ylabel("PMF")

    b = Binomial(0.5, 10)
    x_values = [i for i in range(11)]
    y_values = [b.PMF(x) for x in x_values]
    ax = axes[1, 0]
    ax.bar(x_values, y_values)
    ax.set_title("Binomial(0.5,10)")
    ax.set_xlabel("x")
    ax.set_ylabel("PMF")

    br = Bernoulli(0.7)
    x_values = [0, 1]
    y_values = [br.PMF(x) for x in x_values]
    ax = axes[1, 1]
    ax.bar(x_values, y_values)
    ax.set_title("Bernoulli(0.7)")
    ax.set_xlabel("x")
    ax.set_ylabel("PMF")

    axes[1, 2].set_visible(False)
    plt.tight_layout()
    plt.show()


def plot_parameter_sensitivity(
    distribution_class, param_variants: list, x_range: tuple
):
    fig, ax = plt.subplots(figsize=(10, 6))

    x_start, x_end = x_range
    x_values = [x_start + i * (x_end - x_start) / 200 for i in range(201)]

    for params in param_variants:
        # create distribution with these parameters
        dist = distribution_class(**params)

        # get y values — try PDF first, fall back to PMF
        try:
            y_values = [dist.PDF(x) for x in x_values]
            ax.plot(x_values, y_values, label=str(params))
        except NotImplementedError:
            x_int = list(range(int(x_start), int(x_end) + 1))
            y_values = [dist.PMF(x) for x in x_int]
            ax.bar(x_int, y_values, alpha=0.4, label=str(params))

    ax.set_title(f"Parameter Sensitivity — {distribution_class.__name__}")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability")
    ax.legend()
    plt.tight_layout()
    plt.show()


def plot_sample_convergence(distribution, ns: list):
    """
    ns = [10, 100, 1000, 10000]
    Plots sample mean vs theoretical mean as n grows.
    Shows law of large numbers visually.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sample_means = []
    for n in ns:
        samples = distribution.sample(n)
        sample_means.append(sum(samples) / len(samples))
    ax.plot(ns, sample_means, marker="o", label="Sample Mean")
    ax.axhline(
        y=distribution.mean(), color="r", linestyle="--", label="Theoretical Mean"
    )
    ax.set_title("Sample Convergence")
    ax.set_xlabel("n")
    ax.set_ylabel("Mean")
    ax.legend()
    plt.tight_layout()
    plt.show()


def plot_cdf(distributions: dict, x_range: tuple):
    """
    CDF curves for one or more distributions on same axes.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    x_start, x_end = x_range
    x_values = [x_start + i * (x_end - x_start) / 200 for i in range(501)]
    for name, dist in distributions.items():
        try:
            y_values = [dist.CDF(x) for x in x_values]
            ax.plot(x_values, y_values, label=name)
        except NotImplementedError:
            continue
    ax.set_title("Cumulative Distribution Functions")
    ax.set_xlabel("x")
    ax.set_ylabel("CDF")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


plot_distribution_gallery()

plot_parameter_sensitivity(
    Gaussian,
    [{"mu": 0, "sigma": 0.5}, {"mu": 0, "sigma": 1}, {"mu": 0, "sigma": 2}],
    x_range=(-5, 5),
)

plot_sample_convergence(Gaussian(0, 1), ns=[10, 100, 1000, 10000, 100000])

plot_cdf(
    {
        "Gaussian(0,1)": Gaussian(0, 1),
        "Gaussian(0,2)": Gaussian(0, 2),
        "Exponential(1)": Exponential(1),
    },
    x_range=(-4, 6),
)
