sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# Removing all occurrences of "Pastrami sandwich" using a while loop
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Preparing orders of the clients
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.lower()}")

# Printing the list of sandwiches that were made
print("\nList of sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)
