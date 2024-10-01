#Largest of 3 numbers
a= int(input("Enter first no"))
b= int(input("Enter second no"))
c= int(input("Enter third no"))

grst=a

if b>grst:
    grst=b

elif c>grst:
    grst=c

print(grst)