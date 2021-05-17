#A python program to reverse an Array

#Function to reverse A[] from start to end

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


#Testing the above equation
A = [10,5,6,9]
print("The Original list is: ")
print(A)

#Reverse the list
reverseList(A, 0, 3)

print("The reversed list is: ")
print(A)