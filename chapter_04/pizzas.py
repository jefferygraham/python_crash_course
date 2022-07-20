toppings = ['pepperoni', 'sausage', 'spinach']
friends_toppings = toppings[:]

toppings.append("extra cheese")
friends_toppings.append("cauliflower")

for topping in toppings:
    print(f"I like {topping} pizza!")

print("\n")

for topping in friends_toppings:
    print(f"My friend likes {topping} pizza!")

print("\nWe really like pizza!")
