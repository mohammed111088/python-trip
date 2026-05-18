USD = 1
EUR = 0.99
SAR = 3.75

print("===================\n")
print("welcome to $$ Exchange Store $$")
print("===================\n")

From = input("Exchange FROM (USD, EUR, SAR): ").upper()
Amount = float(input("How much? "))
To = input("Exchange TO (USD, EUR, SAR): ").upper()

NewAmount = 0

if From == To:
    print(f"You will keep your amount as it is, ({Amount} {From})")
    exit()


elif From == "USD" and To == "EUR":
    NewAmount = Amount * EUR
    print(f"You will give {Amount} {From}, and you will take {NewAmount} {To}")

elif From == "USD" and To == "SAR":
    NewAmount = Amount / SAR
    print(f"You will give {Amount} {From}, and you will take {NewAmount} {To}")
elif From == "EUR" and To == "USD":
    NewAmount = Amount / EUR
    print(f"You will give {Amount} {From}, and you will take {NewAmount} {To}")
elif From == "EUR" and To == "SAR":
    NewAmount = Amount / EUR * SAR
    print(f"You will give {Amount} {From}, and you will take {NewAmount} {To}")
elif From == "SAR" and To == "USD":
    NewAmount = Amount / SAR
    print(f"You will give {Amount} {From}, and you will take {NewAmount} {To}")
elif From == "SAR" and To == "EUR":
    NewAmount = Amount / SAR * EUR
    print(f"You will give {Amount} {From}, and you will take {NewAmount} {To}")
else:
    print("You wrote wrong currancy")