month=int(input("enter the month number"))
sussu={4,6,9,11}
pavi={1,3,5,7,8,10,12}
if month==2:
    print("28 days or 29 days")
elif month in sussu:
    print("30 days")
elif month in pavi:
    print("31 days")
else:
    print("invalid month")