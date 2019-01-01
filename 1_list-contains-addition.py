# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def contains_addition(num_list, k):

    for number in num_list:
        value_to_check = k-number
        temp_list = list(num_list)
        temp_list.remove(number)

        if(value_to_check in temp_list):
            return True
    return False


a = [10, 15, 3, 7]
k = 17

print(contains_addition(a, k))