# Predefined name to check against
my_name = "Tamar"

# Loop to continuously ask for the user's name
while True:
    user_name = input("What is your name? ")
    if user_name.lower() == my_name.lower():
        print("Hey, we have the same name!")
        break
    else:
        print(f"Nice to meet you, {user_name}!")

print("Loop ended.")
