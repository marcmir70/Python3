numbers = [1, 2, 3]
pizza_toppings = ["cheese", "pepperoni"]
mixed_lists = [1, "cheese", 2, "pepperoni"]
list_of_lists = [[1,2],[2,3]]

print(pizza_toppings[0])
print(pizza_toppings[-1])
print(pizza_toppings[1])

print(len(pizza_toppings))

pizza_toppings.append("pinneaple")
print(pizza_toppings)

print(pizza_toppings[-1])
print(pizza_toppings[-2])
print(pizza_toppings[1])
print(pizza_toppings[2])

pizza_toppings.insert(0, "mushrooms")
print(pizza_toppings)

del pizza_toppings[0]
print(pizza_toppings)

pizza_toppings.pop()
print(pizza_toppings)

pizza_toppings.remove("cheese")
print(pizza_toppings)

pizza_toppings = ["cheese", "cheese", "pepperoni"]
pizza_toppings.remove("cheese")
print(pizza_toppings)

pizza_toppings = ["cheese", "cheese", "pepperoni", "cheese", "pepperoni"]
pizza_toppings.remove("cheese")
print(pizza_toppings)
