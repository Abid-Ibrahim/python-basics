Min=50
charge=0
d=int(input("Enter the distance:"))
if d <= 10:
   extra1=int(input("Enter the extra charge(<10km) per km:"))
   charge=Min+d*extra1
elif d>10:
   extra2=int(input("Enter the extra charge(>10km) per km:"))
   charge=Min+d*extra2
else:
   charge=Min

print("Taxi charge:",charge)   