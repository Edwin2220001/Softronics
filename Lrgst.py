# Find the largest Element in an Array.
Arr= []
size= int(input("Enter the size"))

for i in range(size):
    Arr.append(int(input("Enter the number")))

lrg= Arr[1]

for i in range(size):
    if Arr[i]> lrg:
        lrg= Arr[i]

print("Largest = ", lrg)        