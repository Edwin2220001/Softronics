Arr=[]

size= int(input("Enter the size "))

for i in range(size):
    Arr.append(int(input("Enter the number")))
i=0

while i <= size:
    j=i+1
    while j<= size-1:
        if Arr[i]>Arr[j]:
            Arr[i],Arr[j]= Arr[j],Arr[i]
        j+=1 

    i+= 1

print("Sorted array is:", Arr)