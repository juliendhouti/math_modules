# Julien Dhouti
# Started: October 30, 2016
# This script is a class of math functions applied to lists.

import NumMath
import BoolFunctions

# Will return the median in a function.
def list_median(li):
    """Returns the median of a given numerical list."""
    li.sort()

    if len(li) % 2 == 0:                # If the length of the list is even,
        fHalf = li[:len(li) / 2]        # Obtain the first half
        sHalf = li[len(li) / 2:]        # and then the second half

        return (fHalf[-1] + sHalf[0]) / 2.0

    else:
        answer = li[:(len(li) / 2) + 1]

        return answer[-1]

def list_sum(li, n = 0):
    """Return the sum of all elements in a given numerical list."""
    if n == len(li) - 1:
        return li[n]

    else:
        return li[n] + list_sum(li, n + 1)

def list_mean(li):
    """Returns the mean of all of the elements in a given numerical list."""

    return list_sum(li) / float(len(li))

def list_range(li):
    """Returns the range of a given numerical list."""
    li.sort() # this is mutation

    return abs(li[-1] - li[0])

def list_prod(li, n = 0):
    """Returns the product of every element in a given numerical list."""
    if n == len(li) - 1:
        return li[n]

    else:
        return li[n] * list_prod(li, n + 1)

def list_sum_square(li):
    """Returns the sum of all of the values in a given numerical list, squared."""
    newList = []

    for i in range(0, len(li)):
        newList.append(myMath.power(li[i], 2))

    return list_sum(newList)

def list_square(li):
    """Returns a list of all of the values from a given numerical list, squared."""
    newList = []

    for i in range(0, len(li)):
        newList.append(myMath.power(li[i], 2))

    return newList

def list_filter_even(li):
    """Returns only the even integers of a given numerical list."""
    newList = []

    for i in range(0, len(li)):
        if myMath.is_even(li[i]):
            newList.append(li[i])

    return newList

def list_filter_True(li):
    """Returns only the true booleans in a given boolean list."""
    newList = []

    for i in range(0, len(li)):
        if BoolFunctions.is_true(li[i]):
            newList.append(li[i])

    return newList

# This is a higher order function
# This will combine two different lists given a basic numerical function
def list_combination(func, l1, l2):
    newList = []
    c = 0

    try:
        for i in range(0, len(l1)):
            newList.append(func(l1[i], l2[c]))
            c += 1

        return newList

    except IndexError:
        return "IndexError"

# This function uses a higher order function
def list_mult_index(l1, l2):
    """Returns the product of each given index in two given numerical list, in one list."""

    return list_combination(NumMath.prod, l1, l2)

# This function uses a higher order function
def list_sum_index(l1, l2):
    """Returns the sum of each given index in two given numerical list, in one list."""

    return list_combination(NumMath.sum, l1, l2)

# This function uses a higher order function
def list_distance_index(l1, l2):
    """Returns the distance between each given index in two given numerical list, in one list."""

    return list_combination(NumMath.distance, l1, l2)

# This is a higher order function!
# This will apply a certain math function to every element in a list.
def list_one_by_one(func, l, n):
    newList = []

    try:
        for i in range(0, len(l)):
            newList.append(func(l[i], n))

        return newList

    except IndexError:
        return "IndexError"

# Mutator method!
def list_inc(l, n):
    """Increments every element in a list by a given number."""

    return list_one_by_one(NumMath.sum, l, n)

# Mutator method!
def list_mult(l, n):
    """Multiplies every element in a given numerical list by a given number."""

    return list_one_by_one(NumMath.prod, l, n)

# Mutator method!
def list_dec(l, n):
    """Deducts a given amount from every element in a list."""

    return list_one_by_one(NumMath.sub, l, n)

def list_eq(l1, l2):
    """Returns True if both given numerical lists are identical. False otherwise."""
    k = 0

    while k < len(l1):
        if l1[k] == l2[k]:
            k += 1

        else:
            return False

    return True

def list_reverse(l):
    """This function returns the reverse of any given numerical lists."""
    i, tlist = -1, []

    try:
        while i >= -1 * len(l):
            tlist.append(l[i])
            i -= 1

        return tlist

    except IndexError:
        return "Index Error!"

def list_range_by_to(start, dec, end):
    """Returns a list of all items between end and start in intervals of dec. Decreasing order."""
    newList, c = [], start

    while c >= end:
        newList.append(c)
        c -= dec

    return newList

def some_even(l):
    """Checks if a numerical list contains any even numbers. Returns True if it does."""
    c = 0

    while c < len(l):
        if l[c] % 2 == 0:
            return True

        else:
            c += 1

    return False

def all_even(l):
    """Checks if a numerical lists ONLY contains even numbers. Returns True if it does."""
    c = 0

    while c < len(l):
        if l[c] % 2 == 0:
            c += 1

        else:
            return False

    return True

# not working
# fix
def list_is_palindrome(l, s = 0, e = -1):
    if s == e:
        return True

    if l[s] != l[e]:
        return False

    return list_is_palindrome(l, s + 1, e - 1)

# this is higher order function
def list_convert(l1, func):
    """Applies a function to every element in a given numerical function."""
    i, newList = 0, []

    try:
        while i < len(l1):
            newList.append(func(l1[i]))
            i += 1

        return newList

    except:
        return "Given function cannot be applied to an integer!"
