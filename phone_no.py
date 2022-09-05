''' this is  a program to 
check if a no. has the correct format

ex: 017-555-1212'''
ph_no=input("enter the phone no.")
v= True
if len(ph_no)!=12:
    v=False
if (ph_no[3]!='-' or ph_no[7]!='-'):
    v=False
for i in range(12):
    if(i==3 or i==7):
        continue
    if(not(ph_no[i].isdigit())):
        v=False
print(v)
