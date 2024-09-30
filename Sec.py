Arr=[]

size= int(input("Enter the size of the array\n"))

for i in range(size):
    Arr.append(int(input("Enter the number")))


for i in range(size):
    for j in range(i+1, size):
        if  Arr[i]>Arr[j] :
            Arr[i], Arr[j]= Arr[j], Arr[i]


SL= Arr[size-2]
print("Second largest number is ",SL)            