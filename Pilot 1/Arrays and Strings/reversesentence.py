#A python program to reverse the string of an array
# Function to reverse the string 
def reverseSentence(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
#driver code
A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
A = "" .join(A)
A = A.split(" ") 
reverseSentence(A,0,2 )
#Reversed List
print('Reverse is:')
A = " " .join(A)

A = [char for char in A]
print(A)

