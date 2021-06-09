def countdown(n):
    while n > 0:
        print(n)
        n -= 1	
    print("Blast off!") 
countdown(5)


# TIME COMPLEXITY 

# #O(n)the loop  runs in linear time 
# #O(1)the time complexity is in constant time 
# #O(n)this runs in linear time 
# #the print function runs in constant time 
# therefore the time complexity of this algorithm is O(n)+O(1)+O(n)
# the time complexity is IN QUADRATIC TIME O(n^2)


# SPACE COMPLEXITY
#  since we have only one variable n that is an int the program
#  runs in constant time O(1)

