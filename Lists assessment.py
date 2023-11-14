print()
print("Welcome to the Royal Chicken")
print()
print("What would you like to order?")
print()
print("We offer the following items:")
print()
items = ['Pizza (£7.30)', 'Pie(£3.45)', 'Burger(£4.50)', 'Chips (£2.00)', 'Onion rings(£2.30)', 'Drink(£1.50)']
print(items)
print()
print("What would you like?")
print()
answer = input("Answer:")
print()
if answer =="Pizza":
    print("Pizza was added to your order. Your total is £7.30")
elif answer =="Pie":
    print("Pie was added to your order. Your total is £3.45")
elif answer =="Burger":
    print("Burger was added to your order. Your total is £4.50")
elif answer =="Chips":
    print("Chips was added to your order. Your total is £2.00")
elif answer =="Onion rings":
    print("Onion rings was added to your order. Your total is £2.30")
elif answer =="Drink":
    print("Drink was added to your order. Your total is £1.50")
print()
print("Would you like to order anything else?")
print()
print("Yes or No")
print()
answer =input("Answer:")
if answer =="No":
    print("Your order will be with you shortly")
elif answer=="Yes":
    print("Please continue with your order")
print()
print("What else would you like?")
print()
answer = input("Answer:")
print()
if answer =="Pizza":
    print("Pizza was added to your order.")
elif answer =="Pie":
    print("Pie was added to your order.")
elif answer =="Burger":
    print("Burger was added to your order.")
elif answer =="Chips":
    print("Chips was added to your order.")
elif answer =="Onion rings":
    print("Onion rings was added to your order.")
elif answer =="Drink":
    print("Drink was added to your order.")
print()
print("Are you finished?")
print("Yes?")
answer =input("Answer:")
if answer=="Yes":
    print("Your items were added to your order your. Your tolat will be sent to you")