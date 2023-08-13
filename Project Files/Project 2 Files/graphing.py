"""Importing the necessary libraries to plotting histograms and boxplots"""
import pandas as pd
import matplotlib.pyplot as plt

# Reading the csv file
data_fr = pd.read_csv('Batting.csv')

"""Creating a Histogram to show National League Batting Average"""
# National League is represented by '0' in the league column, from 1876 to 2017
nat_league_df = data_fr[data_fr['LEAGUE'] == 0]
# Plotting the histogram
plt.hist(nat_league_df['AVERAGE'],  bins=15, density=True)
# Giving the title of the histogram
plt.title("National League Batting Average Histogram")
# Giving the x-axis label
plt.xlabel("Batting Average")
# Giving the y-axis label
plt.ylabel("Relative Frequency")
# Displaying the histogram
plt.show()

"""Creating a Histogram to show American League Batting Average"""
# American League is represented by '1' in the league column, from 1901 to 2017
amer_league_df = data_fr[data_fr['LEAGUE'] == 1]
# Plotting the histogram
plt.hist(amer_league_df['AVERAGE'], bins=15, density=True)
# Giving the title of the histogram
plt.title("American League Batting Average Histogram")
# Giving the x-axis label
plt.xlabel("Batting Average")
# Giving the y-axis label
plt.ylabel("Relative Frequency")
# Displaying the histogram
plt.show()

"""Creating Box Plots for both National and American League Batting Averages"""
# National League is represented by '0' in the league column, from 1876 to 2017
nat_league_df = data_fr[data_fr['LEAGUE'] == 0]
# American League is represented by '1' in the league column, from 1901 to 2017
amer_league_df = data_fr[data_fr['LEAGUE'] == 1]
# Creating a list of the two dataframes
data = [nat_league_df['AVERAGE'], amer_league_df['AVERAGE']]
# Plotting the boxplot
plt.boxplot(data, vert=False)
# Giving the title of the boxplot
plt.title("National and American League Batting Average Boxplots")
# Giving the x-axis label
plt.xlabel("Batting Average")
# Giving the y-axis label
plt.yticks([1, 2], ["National League", "American League"])
# Displaying the boxplot
plt.show()

# Calulcate the mean of the American League Batting Average
amer_league_mean = amer_league_df['AVERAGE'].mean()
# Calculate the median of the American League Batting Average
amer_league_median = amer_league_df['AVERAGE'].median()

# Calculate the mean of the National League Batting Average
nat_league_mean = nat_league_df['AVERAGE'].mean()
# Calculate the median of the National League Batting Average
nat_league_median = nat_league_df['AVERAGE'].median()

# Calculate the standard deviation of the American League Batting Average
amer_league_std = amer_league_df['AVERAGE'].std()
# Calculate the standard deviation of the National League Batting Average
nat_league_std = nat_league_df['AVERAGE'].std()


# print the mean, median, and standard deviation of the American League Batting Average
print("American League Batting Average Mean: ", amer_league_mean)
print("American League Batting Average Median: ", amer_league_median)
print("American League Batting Average Standard Deviation: ", amer_league_std)
# Print the mean, median, and standard deviation of the National League Batting Average
print("National League Batting Average Mean: ", nat_league_mean)
print("National League Batting Average Median: ", nat_league_median)
print("National League Batting Average Standard Deviation: ", nat_league_std)