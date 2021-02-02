##
# Compute and display the edit distance between two strings.
#
# Compute the edit distance between two strings. The edit distance is the minimum number of
# insert, delete and substitute operations needed to transform one string into the other.
# @param s the first string
# @param t the second string
# @return the edit distance between the strings
from functools import lru_cache


@lru_cache(maxsize=None)
def editDistance(s, t):
    # If one string is empty, then the edit distance is one insert operation for each letter in the
    # other string
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        # If the last characters are not equal then set cost to 1
        if s[len(s) - 1] != t[len(t) - 1]:
            cost = 1
        # Compute three distances
        d1 = editDistance(s[0: len(s) - 1], t) + 1
        d2 = editDistance(s, t[0: len(t) - 1]) + 1
        d3 = editDistance(s[0: len(s) - 1], t[0: len(t) - 1]) + \
             cost
        # Return the minimum distance
        return min(d1, d2, d3)


# Compute the edit distance between two strings entered by the user
def main():
    # Read two strings from the user
    s1 = input("Enter a string: ")
    s2 = input("Enter another string: ")
    # Compute and display the edit distance
    print("The edit distance between %s and %s is %d." % \
          (s1, s2, editDistance(s1, s2)))


# Call the main function
main()
