# num=int(input("enter the number to be a pallindrome"))
# temp=num
# rev=0
# while (num>0):
#         rem=num%10
#         rev=rev*10+rem
#         num=num/10
# if temp==num:
#         print("num is a pallindrome")
# else:
#         print("no is not a pallindrome")
n=int(input("enter the last no."))
x=0
i=n
while i>0:
        x+=i
        i-=1
print(x)