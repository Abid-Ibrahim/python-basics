def checkstr():
    sen = input("Enter the sentence: ")
    word = input("Enter the word to searched in sentence: ")
    if word in sen:
        print("Yes, " + word +" is present in "+sen )
    else:
        print("word not present")

checkstr()