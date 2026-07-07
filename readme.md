# Day 6 — Probability Distributions Simulator & Visualizer

Five probability distributions implemented from scratch with sampling, theoretical statistics, and visualisation. No scipy.stats used for core logic.

## Distributions Implemented

| Distribution | Type | Parameters | Use Case |
|---|---|---|---|
| Bernoulli | Discrete | p | Single yes/no trial |
| Binomial | Discrete | n, p | Count of successes in n trials |
| Gaussian | Continuous | μ, σ | Measurements with many small influences |
| Poisson | Discrete | λ | Count of events in fixed interval |
| Exponential | Continuous | λ | Time between events |

## File Structure

```
probability_distribution_simulator/
├── src/
│   ├── distribution.py     # All five distribution classes
│   └── visualizer.py       # Four visualisation functions
├── tests/
│   └── test.py             # 12 tests — all passing
├── demo.py
├── problem_statement.md
├── approach.md
└── learnings.md
```

## Usage

```python
from src.distribution import Gaussian, Poisson, Binomial, Bernoulli, Exponential

# theoretical values
g = Gaussian(mu=0, sigma=1)
g.PDF(0)        # → 0.3989  (peak of bell curve)
g.CDF(0)        # → 0.5     (50% below mean)
g.mean()        # → 0
g.variance()    # → 1

# sampling
samples = g.sample(1000)   # Box-Muller transform

# discrete
b = Binomial(p=0.3, n=10)
b.PMF(3)        # → 0.2668  (probability of exactly 3 successes)
b.CDF(3)        # → 0.6496  (probability of 3 or fewer)
```

## Visualisations

```python
from src.visualizer import (
    plot_distribution_gallery,
    plot_parameter_sensitivity,
    plot_sample_convergence,
    plot_cdf
)

plot_distribution_gallery()

plot_parameter_sensitivity(
    Gaussian,
    [{"mu": 0, "sigma": 0.5}, {"mu": 0, "sigma": 1}, {"mu": 0, "sigma": 2}],
    x_range=(-5, 5)
)

plot_sample_convergence(Gaussian(0, 1), ns=[10, 100, 1000, 10000])

plot_cdf({
    "Gaussian(0,1)": Gaussian(0, 1),
    "Exponential(1)": Exponential(1),
}, x_range=(-3, 5))
```

## Test Results

```
12/12 tests passing
```

## Sampling Methods

- **Gaussian** — Box-Muller transform
- **Exponential** — Inverse CDF method
- **Poisson** — Knuth's algorithm
- **Binomial** — Direct Bernoulli simulation
- **Bernoulli** — Single uniform comparison

## Dependencies

```
matplotlib   (visualisation only)
math         (standard library)
random       (standard library)
```