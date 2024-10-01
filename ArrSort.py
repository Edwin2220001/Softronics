Arr=[]

size= int(input("Enter the size "))

for i in range(size):
    Arr.append(int(input("Enter the number ")))

i=0

while i <= size:
    j=i+1
    while j<= size-1:
        if Arr[i]>Arr[j]:
            Arr[i],Arr[j]= Arr[j],Arr[i]
        j+=1 

    i+= 1

print("Array sorted in ascending order is:", Arr)

i=0

for i in range(size):
    
    for j in range(i+1, size):
        if Arr[j]>Arr[i]:
            Arr[i],Arr[j]= Arr[j],Arr[i]


print("Array sorted in descending order is:",Arr)


# for i in range(size):
#     j=i+1
#     for j in range(size):
#         if Arr[i]> Arr[j]:
#             Arr[i],Arr[j]= Arr[j],Arr[i]


# print("Array sorted in descending order is:", Arr)  