"""
Create a function that generates a one-bit message(in the form of "0" or "1").
Set constants p_0 = 0.35, e_0 = 0.04, or e_1 = 0.05.
The transmitting signal is represented by "S" and the receiving signal is represented by "R".
Output S = 0 when m = np.random.rand() < p_0 and S = 1 when m = np.random.rand() > p_0.
Generate R = 0 when S = 0 and t = np.random.rand() > e_0 or when S = 1 and t = np.random.rand() <= e_1.
Generate R = 1 when S = 0 and t = np.random.rand() <= e_0 or when S = 1 and t = np.random.rand() > e_1.
Now compare the results of S and R. If S = 1 when R = 1, then the experiment is a "success".
Repeat the experiment for 100_000 times and note the number of successes.
Finally, calculate the probability of success by dividing the number of successes by 100_000.
"""

# Importing necessary libraries
import numpy as np

# Setting constants
probability_0 = 0.35
comms_error_0 = 0.04
comms_error_1 = 0.07

def generate_receive_message_S_R():
    """Generates a one-bit message 'S' using a random 
    number and the constants"""

    # Generating a random numbers to be used
    random_num_1 = np.random.rand() # For generating the message
    random_num_2 = np.random.rand() # For generating the receiving signal
    # Setting up the message variable(one-bit message S)
    S = ''
    # Checking if the random number is less than the probability of 0
    if random_num_1 <= probability_0:
        # Setting the message to 0
        S = 0
    else: # If random_num_1 > probability_0
        # Setting the message to 1
        S = 1

    # Setting up the receive variable(one-bit message R)
    R = ''
    # Checking the received signal based on the critierion
    if S == 0:
        if random_num_2 <= comms_error_0:
            R = 1
        else: # If random_num_2 > comms_error_0
            R = 0
    else: # If S == 1
        if random_num_2 <= comms_error_1:
            R = 0
        else: # If random_num_2 > comms_error_1
            R = 1

    # Returning the message and the receiving signal
    return S, R

def experiment():
    """Running the experiment 100,000 times, noting the number of 
    successes and calculating the probability of success"""

    # Setting up the number of times the experiment needs to be run
    num_trials = 100_000
    # Setting up a variable to store the number of successes
    num_successes = 0

    # Setting up the loop to run the experiment 100,000 times
    for _ in range(num_trials):
        # Calling the function to generate the message and the receiving signal
        S, R = generate_receive_message_S_R()
        # Checking the condition "If S = 1 when R = 1"
        if R == 1:
            if S == 1:
                # Incrementing the number of successes
                num_successes += 1

    # Calculating the probability of success
    success_probability = num_successes / num_trials
    # Returning the probability of success
    return success_probability

if __name__ == "__main__":
    # Calling the experiment function
    success_probability = experiment()
    # Printing the probability of success
    print(f"Probability of Success: {success_probability}")
    