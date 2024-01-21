x = float(input("Pierwsza liczba:"))
y = float(input("Druga liczba:"))
operator = input("Operator: +,-,*,/ : ")

if operator =="+":print (x + y)
elif operator == "-":print (x - y)
elif operator == "*":print (x * y)
elif operator == "/":print (x / y)
else:print ("Nieznany operator,sprobuj jeszcze raz")
