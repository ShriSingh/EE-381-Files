"""
Creating a function to roll three identical multi-sided unfair die.
The probability vectors are: p = [0.1, 0.1, 0.1, 0.3, 0.2, 0.2]
Count the number of times you get a "sequence": "One" 
for the 1st die followed by "Two" fort he 2nd die followed by "Three" for the 3rd die.
Conduct the experiment 1000 times and note down the number of "successes".
Use the Poission distribution formula to approximate the probability of getting success.
Consider the np <= 5.
The parameter 'λ' is obtained by multiplying the number of trials by the probability of success.
Create a PMF plot for the Poission distribution formula.
"""

# Importing the required libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Given probability vector for the dice
p = [0.1, 0.1, 0.1, 0.3, 0.2, 0.2]

# Number of rolls and experiments
n = 1000
N = 10000

# Calculate parameter λ for the Poisson distribution
lambda_param = n * (p[0] + p[1] + p[2])

# Initialize an array to store the number of successes in each experiment
successes = np.zeros(N, dtype=int)

# Perform N experiments
for i in range(N):
    # Simulate rolling the dice n times and counting the number of successes
    rolls = np.random.choice(range(1, len(p) + 1), size=n, p=p)
    num_successes = np.sum(rolls == 1)  # Counting "one" for success on the first die
    # Increment the number of successes in the ith experiment
    successes[i] = num_successes

# Create an array of possible values for the random variable X
x_values = np.arange(0, n + 1)

# Calculate the PMF using the Poisson distribution
pmf_poisson = poisson.pmf(x_values, lambda_param)

# Plot a Stem Plot of the PMF of X
plt.stem(x_values, pmf_poisson, use_line_collection=True)
plt.xlabel('Number of Successes in n = 1000 trials')
plt.ylabel('Probability')
plt.title('Bernoulli Trials: PMF - Poisson Approximation', fontweight='bold')
plt.show()