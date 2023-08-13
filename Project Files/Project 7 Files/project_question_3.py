"""
-> Simulate the exponentially distributed random variable 'T', representing 
the lifetime of a carton of n = 30 batteries with the mean(𝜇) and the 
standard deviation(𝜎) to equal 50
-> Conduct the simulation experiment 10,000 times for 10,000 cartons, note 
down the value every time the simulation is conducted, and sum them to 
calculate the random variable 'C'
-> Calculate the experimental PDF(Probability Density Function) for a 
carton of batteries and the plot it 
-> Graph the normal distribution histogram by approximating the 
mean(𝜇_C = n𝜇_T = 𝜇β) and standard deviation(𝜎_C = 𝜎_T(sqrt(n)) = β(sqrt(n)))
and displaying it with the PDF function
-> Plot the CDF(Cumulative Density Function) to find out the lifetime 
of a carton of batteries
-> Find the probability the carton of batteries lasting longer than 
Y1 = 3 years or Y1 = 365 * 3 = 1095 days. 
-> Find the probability the carton of batteries lasting between 
Y2 = 365 * 2 = 730 days and Y3 = 365 * 4 = 1460 days
"""

# Importing the required libaries
import numpy as np
import matplotlib.pyplot as plt

def simulate_rv_values(n, mu, num_experiments):
    """Calculate the random variable 'C' by calculating the 
    sum of thethe exponential distribution of the random 
    variable 'T'"""
    np.random.seed(42)  # for reproducibility
    # Simulate the lifetime of a carton of batteries (T) 10,000 times
    T_simulations = np.random.exponential(scale=mu, size=(num_experiments, n))
    # Calculate the random variable 'C' by summing up the 10,000 simulations
    RANDOM_VARIABLE_C = np.sum(T_simulations, axis=1)
    # Return the random variable 'C'
    return RANDOM_VARIABLE_C

def plot_pdf_and_norm_dist(rv_c, mean_beta_c, std_dev_beta_c):
    '''Calculating and plotting the PDF and the normal distribution'''
    # Creating a histogram of the random variable 'C'
    plt.hist(rv_c, bins=50, density=True, alpha=0.6, color='blue', label='Experimental PDF')
    # Plotting the normal distribution
    norm_dist = np.linspace(mean_beta_c - 3 * std_dev_beta_c, mean_beta_c + 3 * std_dev_beta_c, 100)
    # Calculating the Normal Distribution PDF
    norm_pdf = (1 / (std_dev_beta_c * np.sqrt(2 * np.pi))) * np.exp(-(norm_dist - mean_beta_c)**2 / (2 * std_dev_beta_c**2))
    # Plotting the normal distribution and PDF
    plt.plot(norm_dist, norm_pdf, color='red', label='Approximated Normal Distribution PDF')
    # Setting the title and labels
    plt.title('Experimental PDF against and Corresponding Normal Distribution')
    plt.xlabel('Lifespan of a Carton of Batteries')
    plt.ylabel('Probability Density Function(PDF)')
    plt.legend()
    plt.show()

def plot_cdf(rv_c):
    '''Calculating and plotting the CDF and its Distribution'''
    # Creating a histogram of the random variable 'C'
    plt.hist(rv_c, bins=50, density=True, cumulative=True, alpha=0.6, color='g', label='Experimental CDF')
    # Plotting the CDF
    plt.plot(np.sort(rv_c), np.arange(1, len(rv_c) + 1) / len(rv_c), color='m', label='Theoretical CDF')
    # Setting the title and labels
    plt.title('Experimental CDF and corresponding CDF Distribution')
    plt.xlabel('Lifespan of a Carton of Batteries')
    plt.ylabel('Cumulative Density Function(CDF)')
    plt.legend()
    plt.show()

def calc_p_longer_than_Y1(C, Y1):
    '''Calculating the probability of the carton of
      batteries lasting longer than Y1'''
    prob_longer_than_Y1 = np.sum(C > Y1) / len(C)
    return prob_longer_than_Y1

def calc_p_between_Y2_Y3(C, Y2, Y3):
    '''Calculating the probability of the carton of
      batteries lasting between Y2 and Y3'''
    prob_between_Y2_Y3 = np.sum((C >= Y2) & (C <= Y3)) / len(C)
    return prob_between_Y2_Y3


def main():
    '''Calling up the functions to run the program'''
    # Setting up the parameters
    CARTON_BATTERIES_NUM = 30
    MEAN_BETA = 50
    STD_DEV_BETA = 50
    NUM_EXPERIMENTS = 10000
    DAYS_IN_A_YEAR = 365
    YEAR_SUB_1 = 3 * DAYS_IN_A_YEAR
    YEAR_SUB_2 = 2 * DAYS_IN_A_YEAR
    YEAR_SUB_3 = 4 * DAYS_IN_A_YEAR

    RANDOM_VARIABLE_C = simulate_rv_values(CARTON_BATTERIES_NUM, MEAN_BETA, NUM_EXPERIMENTS)
    MEAN_BETA_C = CARTON_BATTERIES_NUM * MEAN_BETA
    STD_DEV_BETA_C = STD_DEV_BETA * np.sqrt(CARTON_BATTERIES_NUM)

    plot_pdf_and_norm_dist(RANDOM_VARIABLE_C, MEAN_BETA_C, STD_DEV_BETA_C)
    plot_cdf(RANDOM_VARIABLE_C)

    prob_longer_than_Y1 = calc_p_longer_than_Y1(RANDOM_VARIABLE_C, YEAR_SUB_1)
    prob_between_Y2_Y3 = calc_p_between_Y2_Y3(RANDOM_VARIABLE_C, YEAR_SUB_2, YEAR_SUB_3)

    print(f'Probability of the carton of batteries lasting longer than 3 years or {YEAR_SUB_1} days: {prob_longer_than_Y1}')
    print(f'Probability of the carton of batteries lasting between 2 years or {YEAR_SUB_2} days and 4 years or {YEAR_SUB_3} days: {prob_between_Y2_Y3}')

# d
if __name__ == '__main__':
    main()