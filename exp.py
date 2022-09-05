#python program to scrutinize a char
mych=input('please type your char\n')
if (mych.isupper()):
    print("the following character is uppercase letter\n")
    
elif (mych.islower()):
    print("the following character is lowercase letter\n")
elif(mych.isdigit()):
    print("the following character is a digit\n")
else:
    print("this is a special character\n")