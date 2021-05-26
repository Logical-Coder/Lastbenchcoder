print("Welcome to Dominozz pizza")
print("Here the menu")
print("small veg pizza $99 Non-veg $149")
print("medium veg pizza $199 Non-Veg $249")
print("Large veg pizza $249 Non-Veg $299")
sv=99
sn=149
mv=199
mn=249
lv=249
ln=299
total=0
pizza=str(input("Choose size of Pizza, \nS for small \nM for Medium \nL for large"))
type_pizza=str(input("Type of pizza\nV for veg \nN for Non-veg"))
if pizza=="s" and type_pizza=="v":
    total+=sv
elif pizza=="s" and type_pizza=="n":
    total+=sn
elif pizza=="m" and type_pizza=="v":
    total+=mv
elif pizza=="m" and type_pizza=="n":
    total+=mn
elif pizza=="l" and type_pizza=="v":
    total+=lv
elif pizza=="l" and type_pizza=="n":
    total+=ln

print("Soup 2$ and Pepper is 2$")
ps=str(input("would you like to add yes or no:"))
if ps=="yes":
    if pizza=="s":
        total+=2
    elif pizza=="m":
        total+=3
    else:
        total+=5
        
print(f"Your total bill is $ {total}")
     
    