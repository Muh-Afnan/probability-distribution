# Problem Statement

## Why This Day Exists

Every ML algorithm makes assumptions about how data is distributed. Naive Bayes assumes Gaussian or Bernoulli features. Linear regression assumes Gaussian residuals. Neural network loss functions are derived from likelihood functions of specific distributions. You cannot reason about why an algorithm works — or why it fails — without understanding the distributions underneath it.

Day 6 builds that foundation from scratch. No scipy.stats. No numpy shortcuts for sampling. Just the mathematics of each distribution, implemented directly.

## The Goal

Build a simulator and visualiser for five core distributions — Bernoulli, Binomial, Gaussian, Poisson, Exponential — that can:

- Compute theoretical probabilities at any point (PMF/PDF)
- Compute cumulative probabilities (CDF)
- Generate random samples using correct sampling algorithms
- Return theoretical statistics (mean, variance, std)
- Visualise all of the above clearly

## Why From Scratch

Using `scipy.stats.norm.pdf(x)` tells you nothing about what a Gaussian actually is. Writing the coefficient and exponent yourself forces you to see that the bell curve is just an exponential decay of squared distance from the mean. That understanding stays. The function call doesn't.

## The Deeper Question

Before this day, the intuition was: "a distribution describes data." After this day, the correct intuition is: "a distribution is a mathematical object defined by parameters. Data can be sampled from it, or data can be used to estimate its parameters — but the distribution itself has no data."

This distinction matters every time you fit a model.