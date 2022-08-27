bed=int(input("enter your beds"))
girls=int(input("enter girls"))
if bed<girls:
    print("girls are more",girls-bed)
elif girls<bed:
    print("beds is left",bed-girls)
else:
    print("nothing")
    