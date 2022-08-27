# n=int(input("enter the number"))
# i=1
# while i<=n:
#     first_name=input("enter the name")
#     last_name=input("enter the name")
#     mobile_number=int(input("enter the number;"))
#     country=input("enter the number")
#     gender=input("enter the gender")
#     i=i+1
    
def person(**data):
    for k,v in data.items():
        if k=="firstname":
            print(k,";",v)
        elif k=="lastname":
            print(k,":",v)
        elif k=="age":
            print(k,":",v)
        else:
            print(k,":",v)
    print("")
e=1
while e!="0":
    fname=input("enter the fname:")
    lname=input("enter the lname:")
    age=input("enter the age:")
    mobile=int(input("enter the mobile:"))  
    print(" ")
person(firstname=fname,lastname=lname,age=age,mobileno=mobile)
e=input("enter 0 to exit or any key to continue:")
print("")
        