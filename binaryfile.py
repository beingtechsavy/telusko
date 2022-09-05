import pickle
# help(pickle)
# THE PICKLE FUNCTION LITERALLY HAS 2 FUCTIONS
# LOAD CONVERTS FROM BINARY TO TXT
# DUMP CONVERTS FROM TXT TO BINARY
# a=open('arpan.txt.txt','r+')
# b=open('arpan.dat','rb')
# p=a.read()
# print(p)
# f=pickle.dump(p,'wb') 
# 'if there is no data in dat then it will not show'
# print(f)
# a.close()
# b.close()
# import csv



# wap to print last line of the text file
a=open('arpan.txt.txt','r+')
b=a.readlines()
for i in b:
    print(i)
    k=i
print('the last line is ',k)
