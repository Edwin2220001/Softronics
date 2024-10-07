Arr=[]

size= int(input("Enter the size\n"))


for i in range(size):
    Arr.append(int(input("Enter the number")))



for i in range(size):
    
    min = Arr[i]

    for j in range(i+1, size):
        if Arr[j]< min:
            min= Arr[j]

    min, Arr[i]= Arr[i], min


print("Sorted array:", Arr)    