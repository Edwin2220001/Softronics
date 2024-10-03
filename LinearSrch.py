Arr = []  

size= int(input("Enter the size\n"))

for i in range(size):
    Arr.append(int(input("Enter the number ")))


srch= int(input("Enter the element to be searched\n"))
f=0

for i in range(size):
    if Arr[i]== srch:
        print("Search element found at position ",i+1)
        f=1
        break

if f==0:
    print("Element not found")




# Given an unsorted array arr = [34, 8, 23, 56, 12], Write a program to search for the number 23 using linear search.