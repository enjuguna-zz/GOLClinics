def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)):
            A[i] = A[i + 1]
        A[-1] = first_item


# TIME COMPLEXITY 
# ---------------
# The time complexity for this program is O(n^2) since the first loop runs in linear time
# The second loop runs in linear time 
# the initialization runs in constant time 


# SPACE COMPLEXITY 
# --------------
# Since there is new allocation of memory 
# the space might increase linearly
# hence O(n)
