print("Výtejte v kalkulačce! Pro použití mocniny zadejte M a pro odmocninu zadejte O. Pro ukončení zadejte K")
while True:
 number1 = input("První číslo ")
 number2 = input("Druhé číslo ")
 operace = input("Operace ")

 if operace == "+":
  print(int(number1) + int(number2))
 elif operace == "-":
  print(int(number1) - int(number2))
 elif operace == "*":
  print(int(number1) * int(number2))
 elif operace == "/":
  print(int(number1) / int(number2))
 elif operace == "M":
  print(int(number1) * int(number1))
 elif operace == "O":
  print(int(number1) **(1/2))
 elif operace == "K":
   print("Konec"); break 
 elif number1 and number2 == "0":
  print("Nulou nelze dělit")
 else: print("špatná operace")