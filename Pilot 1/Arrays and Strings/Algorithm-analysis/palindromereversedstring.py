def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s


# Time complexity 
# ----------------------
# The program runs in O(n)


# Space complexity
# -----------------
# Space complexity is constant O(1) because memory allocation happens only once 
