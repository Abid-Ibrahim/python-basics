def addlist():
    fruits = ["Apple", "Orange", "Mango"]
    fruit = input("Enter the fruit name:\t")
    fruits.append(fruit)
    print("You have succesfully added \"{}\" into the list".format(fruit))
    print(fruits)
addlist()