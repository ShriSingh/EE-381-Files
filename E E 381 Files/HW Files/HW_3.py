"""This is code used to help me in answer question from HW 3 Assignment"""

# Importing library for calculating standard deviation
import statistics

# Summation operation on two arrays
y_values = [387, 290, 227, 319, 344, 434, 251,
            235, 212, 183, 268, 258, 347, 237, 331, 192]
x_values = [28, 22, 20, 18, 31, 27, 20, 21, 17, 15, 25, 21, 22, 20, 31, 22]

# Summation operation on two arrays
product_sum = 0
for i in range(len(x_values)):
    product_sum += x_values[i] * y_values[i]

# Summation of all x values
x_sum = 0
for i in range(len(x_values)):
    x_sum += x_values[i]

# Summation of all y values
y_sum = 0
for i in range(len(y_values)):
    y_sum += y_values[i]

# Printing product sum
print("Product Sum:", product_sum)
# Printing 'x' sum
print("X Sum:", x_sum)
# Calculating and Printing 'x' mean
print("X Mean:" , x_sum / len(x_values))
# Calculating and printing 'x' standard deviation
x_std = statistics.stdev(x_values)
print("X Standard Deviation:", x_std)

# Printing 'y' sum
print("Y Sum:", y_sum)
# Printing 'y' mean
print("Y Mean:" , y_sum / len(y_values))
# Calculating and printing 'y' standard deviation
y_std = statistics.stdev(y_values)
print("Y Standard Deviation:", y_std)

# Calculating and printing covariance
covariance = (product_sum - ((x_sum * y_sum) / 16)) / 15
print("Covariance:", covariance)
# Calculating and printing correlation coefficient
r_value = covariance / (x_std * y_std)
print("R Value:", r_value)

# Calculating and printing slope and y intercept
slope = r_value * (y_std / x_std)
print("Slope:", slope)
y_intercept = (y_sum / 16) - slope * (x_sum / 16)
print("Y Intercept:", y_intercept)

# Predicting the value of y for x = 20
y = (slope * 20) + y_intercept
print("Predicted Value of Y for X = 20:", y)