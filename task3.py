#Write a Python program to calculate the sum of the numbers in a given tuple. Input: tuples_list = [(1, 2), (3, 4), (5, 6)]


# Given list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Initialize a variable to hold the sum
total_sum = 0

# Iterate through each tuple in the list
for tup in tuples_list:
    # Sum the elements of the tuple and add to total_sum
    total_sum += sum(tup)

# Print the result
print("The sum of the numbers in the given tuple is:", total_sum)
