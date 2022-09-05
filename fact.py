def fact(n):
    k=1
    for i in range (n):
        k*=n
        n-=1
    return k
print(fact(4)*fact(5))
    