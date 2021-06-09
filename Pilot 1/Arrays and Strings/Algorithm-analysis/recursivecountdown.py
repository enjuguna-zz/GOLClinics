def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1)
countdown_recursive(5)


# TIME COMPLEXITY 
# The if statemet runs in O(1) constant time the print statement runs in constant time 
# The print statements run in constant time 
# The recursive call will be O(2^n)

# SPACE COMPLEXITY
# The space complexity of the program  O(n)
# The memory allocation is constnt depending on the input  
