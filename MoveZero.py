Arr=[]

size= int(input("Enter the size\n"))

for i in range(size):
    Arr.append(int(input("Enter the number")))

j = 0
    
for i in range(len(Arr)):
    if Arr[i] != 0:
        Arr[j], Arr[i] = Arr[i], Arr[j]
        j += 1

print(Arr)