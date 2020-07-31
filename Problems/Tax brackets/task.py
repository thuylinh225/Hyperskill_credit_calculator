income = int(input())
if income >= 132407:
    tax = 28
elif income >= 42708:
    tax = 25
elif income >= 15528:
    tax = 15
else:
    tax = 0
amount = round(income * tax / 100)
print(f"The tax for {income} is {tax}%. That is {amount} dollars!")
