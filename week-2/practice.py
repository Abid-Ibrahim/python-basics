def checkstr():
    sen = input("Enter the sentence:\t")
    word = input("Enter the word to searched in sentence: ")
    if word in sen:
        print("Yes, {} is present in {}".format(word,sen)  )
    else:
        print("word not present")

checkstr()