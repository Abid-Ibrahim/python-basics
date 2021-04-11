![banner](https://user-images.githubusercontent.com/55238388/111981947-5f62d080-8b2e-11eb-98a8-e463fddf7a23.jpg)

<h1 align="center">Python Basics - Week 2 - Day 4</h1>


## Slicing strings

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

Example
Get the characters from position 2 to position 5 (not included):

```
b = "Hello, World!"
print(b[2:5])
```

## Slice From the Start

By leaving out the start index, the range will start at the first character:

Example
Get the characters from the start to position 5 (not included):

```
b = "Hello, World!"
print(b[:5])
```

## Slice To the End

By leaving out the end index, the range will go to the end:

Example
Get the characters from position 2, and all the way to the end:

```
b = "Hello, World!"
print(b[2:])
```

## Negative Indexing

Use negative indexes to start the slice from the end of the string:
Example
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2):

```
b = "Hello, World!"
print(b[-5:-2])
```

## Modify strings

Python has a set of built-in methods that you can use on strings.

### Upper Case

Example
The ```upper()``` method returns the string in upper case:

```
a = "Hello, World!"
print(a.upper())
```

### Lower Case

Example
The ```lower()``` method returns the string in lower case:

```
a = "Hello, World!"
print(a.lower())
```

## Remove Whitespace

Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:

```
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
```

## Replace String

Example
The replace() method replaces a string with another string:

```
a = "Hello, World!"
print(a.replace("H", "J"))
```

## Split String

The split() method returns a list where the text between the specified separator becomes the list items.

Example
The split() method splits the string into substrings if it finds instances of the separator:

```
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```

[Check out this link for more such inbuilt string functions](https://www.w3schools.com/python/python_ref_string.asp)

## Python - Escape Characters

### Escape Character

To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

Example
You will get an error if you use double quotes inside a string that is surrounded by double quotes:

```
txt = "We are the so-called "Vikings" from the north."
```

To fix this problem, use the escape character \":

Example
The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

## Python Lists

```
mylist = ["apple", "banana", "cherry"]
```

### List

Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered and unindexed. No duplicate members.
- Dictionary is a collection which is ordered and changeable. No duplicate members.

Lists are created using square brackets:

```
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

## Properties

- Changeable

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

- Ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.

- Allow Duplicates

Since lists are indexed, lists can have items with the same value:

Example
Lists allow duplicate values:

```
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```

## List Length

To determine how many items a list has, use the len() function:

Example
Print the number of items in the list:

```
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```
## List Items - Data Types
List items can be of any data type:

Example
String, int and boolean data types:

```
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

### A list can contain different data types:

Example
A list with strings, integers and boolean values:

```
list1 = ["abc", 34, True, 40, "male"]
```

## Access Items

List items are indexed and you can access them by referring to the index number:

Example
Print the second item of the list:

```
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
```
## Negative Indexing

Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc.

Example
Print the last item of the list:

```
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
```
## Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

Example
Return the third, fourth, and fifth item:

```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
```
```
Note: The search will start at index 2 (included) and end at index 5 (not included).
```
### By leaving out the start value, the range will start at the first item:

Example
This example returns the items from the beginning to, but NOT including, "kiwi":

```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
```

### By leaving out the end value, the range will go on to the end of the list:

Example
This example returns the items from "cherry" to the end:

```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
```

## Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:

Example
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
```
## Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

Example
Check if "apple" is present in the list:

```
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
```


## Change Item Value

To change the value of a specific item, refer to the index number:

Example
Change the second item:

```
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
```

## Change a Range of Item Values

To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

```
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
```
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second value by replacing it with two new values:

```
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
```
```
Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
```

If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:

```
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
```

## Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The ```insert()``` method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:

```
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
```

## Append Items
To add an item to the end of the list, use the append() method:

Example
Using the append() method to append an item:

```
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
```

## Insert Items
To insert a list item at a specified index, use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert an item as the second position:

```
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
```
Note: As a result of the examples above, the lists will now contain 4 items.

## Extend List
To append elements from another list to the current list, use the extend() method.

Example
Add the elements of tropical to thislist:

```
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
```

The elements will be added to the end of the list.

Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

Example
Add elements of a tuple to a list:

```
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
```

## Week 2 assignment:

[learn about operators in python](https://www.w3schools.com/python/python_operators.asp)

[Exercise on python strings](https://www.w3schools.com/python/exercise.asp?filename=exercise_strings1)


