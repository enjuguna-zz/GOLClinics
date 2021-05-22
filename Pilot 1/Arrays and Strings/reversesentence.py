#A python program to reverse the string of an array
# Function to reverse the string 
def reverseSentence(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
#driver code
A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
A = "" .join(A) #this is good
A = A.split(" ") #['this', 'is', 'good']
reverseSentence(A,0,2 ) #['good', 'is', 'this']
#Reversed List
print('Reverse is:')
A = " " .join(A) #good is this

A = [char for char in A] #['g', 'o', 'o', 'd', ' ', 'i', 's', ' ', 't', 'h', 'i', 's']
print(A)

