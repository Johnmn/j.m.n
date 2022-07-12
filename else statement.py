qty = int(input("Quantity: "))

price = 100 * qty

if qty >1000:

    price = (100 - 0.10 * 100) * qty

print("Cost: Ksh. "+str(price))


scores = int(input("marks"))
if scores >= 70 and  scores <= 100:
        print('A')
elif scores >= 60 and scores <= 69:
        print ('B')
elif scores >= 50 and scores <= 59:
        print('C')
elif scores >= 40 and scores <= 49:
        print('D')
else:
        print("E")
