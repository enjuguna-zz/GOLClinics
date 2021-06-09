def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result



# Time complexity 
# -------------
# The time complexity for the first loop occurs in linear time the second loop also happens in linear time 
# Therefore the time complexity for the program is O(n)


# Space complexity 
# --------------
# Since there is a new memory location result, the memory space might increase and the space complexity is O(n)
