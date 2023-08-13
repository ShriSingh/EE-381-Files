"""
Writing code for the tossing 100 coins and noting the number of heads and tails. 
If the toss gets exactly 50 heads, then the toss is a "success".
Repeat the experiment for 100_000 times and note the number of successes.
"""

# Importing necessary libraries
import numpy as np


def toss_100_coins(repeats):
    '''Creating a function to toss 100 coins and note the number of heads and tails'''
    # Creating a list to store the number of heads
    heads = []
    # Creating a list to store the number of tails
    tails = []
    # Creating a list to store the number of successes
    success = []
    # Number of coin tosses
    coin_toss_num = 100

    # Creating a for loop to toss 100 coins and note the number of heads and tails
    for _ in range(repeats):
        # Creating a list to store the result of 100 coin tosses
        coin = np.random.randint(0, 2, coin_toss_num)  # --> 0 is tails, 1 is heads
        # Appending the number of heads to the heads list
        heads.append(sum(coin))
        # Appending the number of tails to the tails list
        tails.append(100 - sum(coin))
        # Checking if the number of heads is exactly 50
        if sum(coin) == 50:  # --> sum of coins is 50 as 50 = 50 heads
            # Appending 1 to the success list
            success.append(1)
        else:
            # Appending 0 to the success list
            success.append(0)

    # Probability of heads
    p_heads = (sum(heads)/repeats) / 100
    # Probability of tails
    p_tails = (sum(tails)/repeats) / 100
    # Total number of successes
    total_success = sum(success)
    # Probability of successes
    p_success = total_success/repeats

    # Printing the probability of heads
    print("Probability of heads: ", p_heads)
    # Printing the probability of tails
    print("Probability of tails: ", p_tails)
    # Printing the total number of successes
    print("Number of successes: ", total_success)
    # Probability of successes
    print("Probability of successes: ", p_success)


# Calling the function
toss_100_coins(100000)
