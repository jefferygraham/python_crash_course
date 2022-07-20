my_foods = ["pizza", "falafel", "carrot cake"]
# friend_foods = my_foods
friend_foods = my_foods[:]

my_foods.append("ice cream")
friend_foods.append("cannoli")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy Friend's favorite foods are:")
for food in friend_foods:
    print(food)
