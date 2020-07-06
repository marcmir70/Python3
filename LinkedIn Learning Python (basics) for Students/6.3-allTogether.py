# Expected output
# Welcome to Julie's Pizzeria
# Our Available Toppings are:
# Cheese (Free)
# Pepperoni ($1 Extra)

pizza_toppings = ["cheese", "pepperoni"]

def format_topping(topping):
    if topping == "cheese":
        return f"{topping.title()} (Free)"
    else:
        return f"{topping.title()} ($1 Extra)"

# print(format_topping("cheese") == "Cheese (Free)")
# print(format_topping("pepperoni") == "Pepperoni ($1 Extra)")

def print_menu(toppings):
    print("Welcome to Julie's Pizzeria")
    print("Our available toppings are:")
    for topping in toppings:
        print(format_topping(topping))

print_menu(pizza_toppings)
