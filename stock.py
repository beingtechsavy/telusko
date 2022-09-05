# the program to check the amount
# 30% of 1400 is 420
# 420/60 is 7 rs
# target should be of 1:2
risk=100
entry=int(input("enter the entry amount\n"))
stoploss= (90/100)*entry
rupeestop=entry-stoploss
quantity=int(entry/rupeestop)
if entry*quantity>=1400:
    quantity=int(1400/entry)
print('your stoploss is \t',stoploss)
print('the quantity you should buy is\t',quantity)
print('max risk shoukd be',risk)
print('the target is \t',1.10*entry)

