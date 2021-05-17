#A python program to reverse the string of an array
# Function to reverse the string 
def reverseString(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
#driver code
A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
A = "" .join(A)
A = A.split() 
reverseString(A,0, 2 )
#Reversed List
print('Reverse is:')
print(A)

