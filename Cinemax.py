# Function to calculate ticket price based on age
def calculate_ticket_price(age):
    if age < 3:
        return 0
    elif 3 <= age <= 12:
        return 10
    else:
        return 15

# Ask the family the age of each person who wants a ticket
num_family_members = int(input("How many family members want tickets? "))
family_tickets_cost = 0

for _ in range(num_family_members):
    age = int(input("Enter the age of a family member: "))
    ticket_price = calculate_ticket_price(age)
    family_tickets_cost += ticket_price

print(f"\nTotal cost for all family tickets: ${family_tickets_cost}")

# List of teenagers with names and ages
teenagers = [
    {"name": "John", "age": 18},
    {"name": "Emily", "age": 15},
    {"name": "Michael", "age": 21},
    {"name": "Sophia", "age": 16},
    {"name": "Jacob", "age": 14}
]

# Filter out teenagers who are not permitted to watch the movie
allowed_ages = range(16, 22)  # Ages between 16 and 21 (inclusive) are allowed
teenagers = [teenager for teenager in teenagers if teenager["age"] in allowed_ages]

# Print the final list of teenagers who can watch the movie
print("\nList of teenagers allowed to watch the movie:")
for teenager in teenagers:
    print(f"{teenager['name']} - {teenager['age']} years old")
