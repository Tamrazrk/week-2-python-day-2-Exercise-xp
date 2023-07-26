# Create a set called my_fav_numbers with your favorite numbers
my_fav_numbers = {5, 12, 7, 20}

# Add two new numbers to the set
my_fav_numbers.add(10)
my_fav_numbers.add(3)

# Remove the last number
my_fav_numbers.remove(3)  # Assuming 3 is the last number added

# Create a set called friend_fav_numbers with your friend's favorite numbers
friend_fav_numbers = {8, 15, 12, 7}

# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

# Print the sets and the concatenated set
print("My favorite numbers:", my_fav_numbers)
print("Friend's favorite numbers:", friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)
