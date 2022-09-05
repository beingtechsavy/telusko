# this is an program to demonstrate bubble sort
l=[5,7,1,3,98,2,54,65]
n= len(l)
for i in range(n):
    for j in range(n-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
print("the sorted list is",l) 