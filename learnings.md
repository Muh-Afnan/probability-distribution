# Learnings

## The Most Important Insight — Distributions Don't Contain Data

Before this day, the mental model was: "a distribution describes data — you put data in, you get probabilities out."

This is wrong, and it matters.

A distribution is a mathematical object defined entirely by its parameters. `Gaussian(mu=0, sigma=1)` exists independently of any data. It has a shape, a mean, a variance, a way of generating samples — all derived from the parameters alone.

Data and distributions relate in two directions:
- You can **sample from** a distribution to generate data
- You can **fit a distribution to** data to estimate its parameters

But the distribution itself never contains data. Writing `Gaussian(mu, sigma)` instead of `Distribution(data)` made this concrete in a way that reading about it never did.

This distinction matters every time you fit a model. When you fit a linear regression, you are estimating the parameters of a Gaussian distribution over the residuals. When you do Naive Bayes, you are estimating the parameters of a Gaussian or Bernoulli for each feature. The model fitting is parameter estimation — not the distribution itself.

---

## CDF Was the Hardest Concept

PMF and PDF were intuitive — "how probable is this specific value?"

CDF took longer. The confusion was: what does "cumulative" actually mean?

The answer that made it click: CDF answers a different question. Not "how probable is exactly x?" but "what fraction of all outcomes fall at or below x?"

```
CDF(8) on Binomial(n=10, p=0.5) = 0.989
"98.9% of the time you get 8 or fewer heads in 10 flips"
```

Once understood as "probability of everything up to and including x," the implementation became obvious — sum the PMF values from 0 to x.

---

## PMF vs PDF — The Discrete/Continuous Divide

Discrete distributions have probability **mass** — you can ask "what is the probability of exactly 3 events?" and get a meaningful non-zero answer.

Continuous distributions have probability **density** — the probability of exactly any specific value is zero. PDF(1.5) doesn't give you a probability — it gives you the height of the curve. The actual probability lives in areas under the curve, not at points.

This is why CDF matters more for continuous distributions than for discrete ones.

---

## Sampling Algorithms Are Not Arbitrary

Early assumption: sampling just means `random() * some_scale_factor`.

Wrong. Each distribution has a correct sampling algorithm derived from its mathematical structure.

Box-Muller for Gaussian is elegant — two uniform samples, a logarithm and a cosine, and you get a Gaussian. This works because of a deep geometric relationship between the uniform distribution on a disk and the Gaussian distribution in polar coordinates.

Knuth's algorithm for Poisson simulates the actual physical process — counting events until the probability product drops below a threshold.

The algorithms are not tricks. They are consequences of what the distributions actually are.

---

## Formulas — Structure Matters More Than Memorisation

The exact formulas are less important than understanding their structure:

- **Gaussian**: exponential of negative squared distance from mean — that squared term is why it's bell-shaped and symmetric
- **Poisson**: `e^(-λ)` is the probability of zero events, `λ^k/k!` counts the ways k events can arrange — together they give exact count probabilities
- **Exponential**: `λe^(-λx)` — the λ out front normalises it, the exponential decay means events become less likely the longer you wait

Remembering the structure lets you reconstruct the formula when needed. Memorising symbols without structure is fragile.