# Ask the user to input their favorite fruit(s) separated by a space
favorite_fruits_input = input("Please enter your favorite fruit(s) separated by a space: ")

# Convert the input string of words into a list of words (favorite fruits)
favorite_fruits_list = favorite_fruits_input.split()

# Ask the user to input a name of any fruit
chosen_fruit = input("Now, enter the name of any fruit: ")

# Check if the user's input is in the favorite fruits list
if chosen_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")
