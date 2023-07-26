# Initialize the list of pizza toppings
pizza_toppings = []

# Define the base price of the pizza and the price per topping
base_price = 10
topping_price = 2.5

# Ask the user to enter a series of pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping.lower() == 'quit':
        break

    # Add the topping to the list and print a message
    pizza_toppings.append(topping)
    print(f"Adding '{topping}' to your pizza.")

# Calculate the total price
total_price = base_price + (len(pizza_toppings) * topping_price)

# Print the toppings and the total price of the pizza
print("\nYour pizza includes the following toppings:")
for topping in pizza_toppings:
    print("-", topping)

print(f"\nTotal price: ${total_price:.2f}")
