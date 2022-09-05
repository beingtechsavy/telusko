a=4
r=0.5
b=1
n=10000000000
g=1
def tn(n):
    r=0.5
    b=1
    for i in range(1,n):
        b *= r**i
    c=a*b
    return c
for i in range(n):
    g+=tn(i)
print(g)
