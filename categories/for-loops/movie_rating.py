# Babu Macharia
# Get movie rating from a user

"""

This function is a basic movie rating system that asks users for a movie rating between 1 to 5 stars, with being the lowest and 5 being the highest rating.  Also the function is to Print the difference bretween the user ratig and my rating

"""

"""
  Note to self I can write this as a function, but this for educational purposes
  As I move on I willl be writing full fledge functions


"""
# I used the int() to convert the input string to an integer
rating = int(input("Please give me a rating of your favorite movie between 1 to 5  "))
my_rating = 4

print("Your rating is: " ,rating, "\n" "My rating is : ", my_rating)
if rating == my_rating:
    print("We have the same rating!!!!!!!!!!")
elif rating > my_rating:
    print("Your rating is higher than mine by a difference of ", rating - my_rating)