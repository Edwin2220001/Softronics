Arr=[]
size= int(input("Enter the size "))
for i in range(size):
    Arr.append(int(input("Enter number ")))

srch= int(input("Enter the element to be searched\n"))
  
for i in range(size):
    if Arr[i]== srch:
        f=1
        break

print(srch,"found at position", i+1)