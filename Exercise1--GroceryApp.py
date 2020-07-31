print("Hello! Welcome to my Grocery App in Python")
grocery_list = []
print("Enter your 5 grocery items:")
a = input()
b = input() 
c = input()
d = input()
e = input()

grocery_list.append(a)
grocery_list.append(b)
grocery_list.append(c)
grocery_list.append(d)
grocery_list.append(e)

for items in grocery_list:
    print("You have to buy", items)


