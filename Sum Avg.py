Arr= []
size= int(input("Enter the size"))

for i in range(size):
    Arr.append(int(input("Enter the number")))

sum=0

for i in range(size):
    sum= sum+ Arr[i]

print("The sum= ", sum)       

Avg= sum/size
print("Average= ", Avg)