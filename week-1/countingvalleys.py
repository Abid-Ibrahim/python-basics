

def countingValleys(steps, path):
    sealevel = valley = 0
    for i in path:
        if i == "U":
            sealevel += 1
        else:
            sealevel -= 1
        if i == "U" and sealevel == 0:
            valley += 1
    print(valley)





'''
Test case 1:
8
UDDDUDUU
expected output : 1

Test case 2:
12
DDUUDDUDUUUD
expected output : 2
'''


countingValleys(8, "UDDDUDUU")
countingValleys(12,"DDUUDDUDUUUD")


