import string

# STRING FUNCTIONS 
# JOIN
# STR1.JOIN(STR2)
'A0'.join('bc')

# SPLIT
# STR1.SPLIT(CHAR/STRING)
# it is case sensitive
a='AGENT BINOD'.split('N')
print(a)

# REPLACE
# STR1.REPLACE(STR2,STR3)
# STR2 BELONGS TO STR1
b='chamatkar'.replace('c','b')
print(b)
# ////////      THESE FUNC. DONT CHANGE THE VALUE OF STRING ORIGINALLY          ////////
c=string.capwords(b,sep='t')
print(c)