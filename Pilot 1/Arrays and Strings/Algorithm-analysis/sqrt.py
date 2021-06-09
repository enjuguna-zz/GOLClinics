  
def int_sqrt(x):
    for i in range(x):
        if i * i == x:
            return i
    
    return -1



# TIME COMPLEXITY 
# -------------
# The loop runs in linear time 
# The if statement is done in constant time with respect to the loop that runs in linear time O(n)
# There for the time complexity for the program is O(n), this is slower than the bisection method since it has to check every value 


# SPACE COMPLEXITY 
# ---------------
# The memory allocation is is constant since initalisation occurs once 
# hence the space complexity is O(1)
