#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to eliminate duplicate values
    uniq_values = set(my_list)

    # Add all unique values together
    total = sum(uniq_values)

    return total
