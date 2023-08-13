"""
Writing a program that generates a 70_000 * k element list 
of 4-letter passwords using the 26 lowercase letters 
to test against a set 4-letter password. Repeat the test 
for a 1000 times and note the number and the probability of successes.
"""

# Importing necessary libraries
import random
import time

def hacker_password_generator():
    """Creating a function to generate a hacker's password candidate 
    of 4-letter passwords using the 26 lowercase letters"""
    alaphabets = "abcdefghijklmnopqrstuvwxyz"
    hacker_password = ""
    for _ in range(4):
        hacker_password += random.choice(alaphabets)
    return hacker_password


def hacker_password_list(elements):
    """Storing the hacker's password candidates in a list"""
    passwords_list = []
    for _ in range(elements):
        passwords_list.append(hacker_password_generator())
    return passwords_list


def hacker_password_test(password, elements, num_repeats):
    """Creating a function to test the hacker's password candidate 
    against a set 4-letter password"""
    password_match = 0
    # Repeating the test for a given number of times
    for _ in range(num_repeats):
        # Checks if the password is in the list
        if password in hacker_password_list(elements):
            # If the password matches, then increment the matching counter
            password_match += 1

    # Calculating the probability of matching success
    matching_probability = password_match / num_repeats
    # Returning the probability of matching success
    return matching_probability

def calculate_least_amount_of_words(password, num_repeats, target_probability):
    """Calculates the least amount of words required to obtain a 50% password match success rate."""
    # Intializing the probability
    probability = 0
    # Intializing the minimum number of words
    min_num_words = 1
    # Looping until the probability is around 50% target probability
    while probability < target_probability:
        # Calling the hacker_password_test function
        probability = hacker_password_test(password, min_num_words * min_num_words, num_repeats)
        # Incrementing the minimum number of words
        min_num_words += 1
    # Returning the minimum number of words
    return min_num_words


# Setting a 4-letter password
set_password = "qfmp"
# Setting the number of elements in the list
elements = 70000
elements_1 = 70000 * 1 # k * m, '1' here represents when k = 1
elements_2 = 70000 * 7 # k * m, '7' here represents when k = 7
# Setting the number of repeated trials
num_repeats = 1000
# Setting the target probability of matching success
target_probability = 0.5
# Calling the functions
password_matching_probability = hacker_password_test(set_password, elements, num_repeats)
password_matching_probability_1 = hacker_password_test(set_password, elements_1, num_repeats)
password_matching_probability_2 = hacker_password_test(set_password, elements_2, num_repeats)
# Calling the function to calculate the least amount of words
min_num_words_probability = calculate_least_amount_of_words(set_password, num_repeats, target_probability)
# Printing the processing time
print(f"Processing time: {time.process_time()} seconds")
# Printing the results
print(f"Probability of password matching success: {password_matching_probability}")
print(f"Probability of password matching success when k = 1: {password_matching_probability_1}")
print(f"Probability of password matching success when k = 7: {password_matching_probability_2}")
print(f"Minimum number of words required to obtain a 50% password match success rate: {min_num_words_probability}")