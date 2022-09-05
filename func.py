# functions-mini program or sub program 
# syntax:--- def func(x,y)--->> formal parameters or arguments
#                  x=x+y--->actual parameters or arguments
# difference between parameters and arguments-->>>
# parameters are values pre assigned
# arguments are values passed
# flow of control is always from the main 
# any parameter cant have default values until all the parameters on its right have default values
# named arguments also follow the right most rule
# return stores the variable and also shows the called variable

# def cube(num=2):
#     print(num*num*num)

# #wap to sum 2 no.s using return
# a=int(input("enter no. 1\n"))
# b=int(input("enter no. 2\n"))
# def sum(x=0,y=0):
#     return x+y
# a=sum(a,b)
# print(a)    
# A VOID FUNCTION RETURUNS NONE(FUNCTIONS WITH ONLY PRINT STATEMENT)
# WAP TO CALCULATE CUBE OF A NO. DEFAULT IS 2

# num=int(input("enter the no. to be cubed"))
# cube()
# write a func to check if 2 stringd have same length
# a=input("s1\n")
# b=input("s2\n")
# def lencheck(x,y):
#     if len(a)==len(b):
#         print("True")
#     else:
#         print("False")
# lencheck(a,b)
# wap to compare 2 no.s and print the maximum ones digit
a=int(input("enter the no."))

b=int(input("enter the no."))
def onescomp(x,y):
    x=x%10
    y=y%10
    if x>y:
       print("the biiger one digit is of ",x)
    elif x==y:
        print("they are equal")
    else:
        print("the biiger one digit is of ",y) 
onescomp(a,b)