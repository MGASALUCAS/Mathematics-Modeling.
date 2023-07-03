# Given an array of integers, where all elements but one occur twice, find the unique element.
import numpy as np
import math
import os
import random
import re
import sys

# Function to find the element that occur only once
def lonelyinteger(a):
    # Initialize the value of result
    for i in a:
        if a.count(i) == 1:
            return i
    return None

# Driver code
if __name__ == "__main__":
    # input array
    a = [1, 2, 3, 4, 3, 2, 1]

    # Calling the function
    print(lonelyinteger(a))

