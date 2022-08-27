age=int(input("enter the age:"))
gender=input("enter the gender:")
if age<45 and gender=="male":
    print("any where")
elif age>45 and gender=="male":
    print("urban area")
elif age<15 and (gender=="male" or gender=="female"):
    print("not allow")
elif age>15 and gender=="female":
    print("urban area for female")
else:
    print("enter proper details")
    





















       
       
       
       
       