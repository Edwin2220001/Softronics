Arr = []  

size= int(input("Enter the size "))

for i in range(size):
    Arr.append(int(input("Enter the number ")))

Arr.sort()

x= int(input("Enter the element to be searched\n"))
 

low = 0
high = size - 1

found = False

while low <= high:
    mid = (low + high) // 2
    
    if Arr[mid] == x:
        print(f"Element {x} found at position {mid+1}.")
        found = True
        break
    elif Arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"Element {x} is not present in the array.")