import sys
a=open('arpan.txt.txt','r')
f1=a.readline()
f2=a.readline()
print(f1,f2,sep='\n')
# print(a.readline()) ;'it always stars with the second line '
# for i in range(3):
#     print(a.readline())
# print(a.readline())
# The more we use the readline feature it prints always the next line
# f=a.readline()
# count=1
# note that this wont work directly in a loop with indirect variable
# while f:
#     print(f)
#     count+=1
#     print(count)
#     if count>=10:
#         break
# a.write('hello everyone  I am arpan 4839 a bot from future how are u?')


# another way
# for i in a:
    # print(i)
sys.stdout.write(f1)
sys.stdout.write(f2)