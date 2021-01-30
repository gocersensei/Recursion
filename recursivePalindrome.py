##
# Determine whether or not a string entered by the user is a palindrome using recursion.
#

# Determine whether or not a string is a palindrome
# @param s the string to check
# @return True if the string is a palindrome, False otherwise
def isPalindrome(s):
    # Base case: The empty string is a palindrome. So is a string containing only 1 character.
    if len(s) <= 1:
        return True
    # Recursive case: The string is a palindrome only if the first and last characters match, and
    # the rest of the string is a palindrome
    return s[0] == s[len(s) - 1] and \
        isPalindrome(s[1: len(s) - 1])


# Check whether or not a string entered by the user is a palindrome
def main():
    # Read the string from the user
    line = input("Enter a string: ")

    # Check its status and display the result
    if isPalindrome(line):
        print("That was a palindrome!")

    else:
        print("That is not a palindrome.")


# Call the main function
main()
