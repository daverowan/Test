def calculate_price(size, toppings, extra_sauce):
    # Set base prices based on size
    if size == 'small':
        base_price = 7.00
        topping_price = 0.50
    elif size == 'medium':
        base_price = 10.75
        topping_price = 1.00
    elif size == 'large':
        base_price = 14.75
        topping_price = 1.50
    else:
        print("Invalid size entered.")
        return 0  # Return 0 if the size is invalid

    # Calculate total price
    total_price = base_price + (topping_price * toppings)

    # Add extra sauce cost if requested
    if extra_sauce == 'y':
        total_price += 0.50

    return total_price


# Initialize subtotal
subtotal = 0

# Get number of pizzas
num_pizzas = int(input("How many pizzas would you like? "))

for i in range(num_pizzas):  # Loop through each pizza
    print(f"\nFor pizza {i + 1}:")

    # Get size of pizza
    size = input("What size pizza would you like? (small, medium, large): ")

    # Get number of toppings
    toppings = int(input("How many toppings would you like? "))

    # Ask about extra sauce
    extra_sauce = input("Would you like extra sauce for $0.50? (y/n) ")

    # Calculate price
    pizza_price = calculate_price(size, toppings, extra_sauce)

    if pizza_price > 0: # Only if positive number
        # Print the details of the order
        if extra_sauce == 'y':
            print(f"A {size} pizza with {toppings} toppings and extra sauce is ${pizza_price:.2f}")
        else:
            print(f"A {size} pizza with {toppings} toppings is ${pizza_price:.2f}")


