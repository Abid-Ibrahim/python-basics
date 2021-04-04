a = True
b = False
c = False
  
if a or b and c:
    print ("output 1")
else:
    print ("output 2")

'''

a = True
b = False
c = False
  
if not a or b:
    print (1)
elif not a or not b and c:
    print (2)
elif not a or b or not b and a:
    print (3)
else:
    print (4)


count = 1 
  
def doThis():
  
    global count
  
    for i in (1, 2, 3): 
        count += 1
  
doThis()
  
print (count)
'''