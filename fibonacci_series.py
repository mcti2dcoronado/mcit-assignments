# Write a Python program to generate the Fibonacci series.
# The program should take an input value from the user to determine how many numbers in the series to generate.
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding numbers in the sequence.

# Print Fibonacci Series in Python
# Using Recursion Function 
# F(n) = F(n-1) + F(n-2)
# n = 4
# F(4) = F(4-1) + F(4-2)
# F(4) = 3 + 2 = 5

# Optimizing the recursive Algorithm for the Fibonacci Sequence
# Memoizing: store the results of previous calls in something like 
# a memory cache, using Python list to store the results 
# of previous computations

# Memoization speeds up the execution of expensive recursive functions 
# by storing previously calculated results in a cache.

# Python dictionary
cache = {0: 0, 1: 1}

# Recursive function
def fibonacci_series(serie):
    if serie in cache:
        return cache[serie]
    # Compute and cache the Fibonacci number
    cache[serie] = fibonacci_series(serie - 1) + fibonacci_series(serie - 2)
    return cache[serie]

# limit for the series
limit = 15

for number in range(limit):
    print(fibonacci_series(number))
    
