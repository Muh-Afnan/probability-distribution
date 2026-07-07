# Approach

## Design Decision — Parameters, Not Data

Each distribution class takes only parameters — `Gaussian(mu=0, sigma=1)`, `Poisson(lam=3)`. No data is ever passed in. This is the correct design and reflects how distributions actually work mathematically.

The alternative — passing data to compute an empirical distribution — is a different concept entirely (kernel density estimation). Keeping these separate was an explicit decision.

## Class Structure

Every distribution implements the same interface:

```
PMF(x)     — probability mass at x (discrete only)
PDF(x)     — probability density at x (continuous only)
CDF(x)     — cumulative probability up to x
sample(n)  — generate n random values
mean()     — theoretical mean from formula
variance() — theoretical variance from formula
std()      — theoretical standard deviation
```

Discrete distributions raise `NotImplementedError` on `PDF`. Continuous distributions raise `NotImplementedError` on `PMF`. This enforces correct usage.

## Sampling Algorithms

Each distribution uses the mathematically correct sampling method — not `random.uniform` scaled arbitrarily.

**Gaussian — Box-Muller transform:**
Takes two uniform random values, transforms them into two independent Gaussian samples via:
```
z = sqrt(-2 * log(u1)) * cos(2π * u2)
```
This works because of the relationship between uniform, exponential, and Gaussian distributions in polar coordinates.

**Exponential — Inverse CDF method:**
```
x = -log(u) / λ
```
If U is uniform on [0,1], then -log(U)/λ follows an Exponential(λ) distribution. Derived by inverting the CDF.

**Poisson — Knuth's algorithm:**
Simulates the number of events in a unit interval by multiplying uniform samples until their product falls below `e^(-λ)`. Counts how many multiplications were needed.

**Binomial — Direct simulation:**
Run n Bernoulli trials, count successes. Simple and correct.

## Visualiser Design

Four functions, each with a single clear purpose:

- `plot_distribution_gallery` — overview of all five distributions
- `plot_parameter_sensitivity` — how changing parameters shifts shape
- `plot_sample_convergence` — law of large numbers made visual
- `plot_cdf` — compare CDF curves across distributions

Continuous distributions use line plots. Discrete distributions use bar charts. This distinction is not stylistic — a line between discrete points implies values at non-integer positions which don't exist.

## CDF Implementation

Discrete CDF sums PMF values from 0 to x:
```python
sum(self.PMF(k) for k in range(int(x) + 1))
```

Gaussian CDF uses the error function approximation — no integration needed:
```python
0.5 * (1 + erf((x - mu) / (sigma * sqrt(2))))
```

Exponential CDF has a closed form:
```python
1 - exp(-λx)
```