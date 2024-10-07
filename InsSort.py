Arr=[]

size= int(input("Enter the size\n"))


for i in range(size):
    Arr.append(int(input("Enter the number")))


for i in range(1, size):
    key = Arr[i]
    j = i - 1


    while j >= 0 and key < Arr[j]:
        Arr[j + 1] = Arr[j]
        j -= 1

    Arr[j + 1] = key


print("Sorted array:", Arr)