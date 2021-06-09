#Integer square root bisection method
def int_sqrt_bisect(x):
    low = 0 # O(1)
    high = x # O(1)
    guess = x // 2 # O(1)
    while True: #O(n)
        diff = guess * guess - x
        if diff == 0: # O(1)
            return guess
        if diff < 0: # our guess was lower than the true square root # O(1)
            low = guess # so we should continue searching in the range [guess - high]
        else: # our diff was higher than the true square root
            high = guess # we continue searching in the range [low - guess]
        
        if high - low <= 1: # at this point we can't an integer square root for x
            break

        guess = (low + high) // 2 # pick a guess in the middle of the new range
    return -1



# TIME COMPLEXITY 
# -------------
# The loop runs in linear time 
# The if statement is done in constant time with respect to the loop that runs in linear time O(n)
# There for the time complexity for the program is O(n), this is slower than the bisection method since it has to check every value 


# SPACE COMPLEXITY 
# ---------------
# The memory allocation is is constant since initalisation occurs more than  once 
# hence the space complexity is O(n)