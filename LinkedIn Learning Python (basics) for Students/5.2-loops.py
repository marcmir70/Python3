pizza_toppings = ["cheese", "pepperoni", "mushrooms"]
print(pizza_toppings)

for topping in pizza_toppings:
    print(topping)

for topping in pizza_toppings:
    message = f"I would like {topping} on my pizza"
    print(message)

my_numbers = [1, 2, 3]
my_square_numbers = []
for number in my_numbers:
    my_square_numbers.append(number**2)
print(my_square_numbers)

print("__Suggested Exercise__")
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_numbers:
    if number % 2 == 0:
        print(number)

print("__Suggested Exercise__")
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in my_numbers:
    if number % 2 == 1:
        print(number)
