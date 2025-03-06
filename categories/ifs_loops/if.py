# Reading if statements
# by Babu


# What does the following code below 
# 1. Monday?
# 2. Saturday?
# 3. Sunday?
# 4. Raining

Dow = input("What day is it? ")

# take user input and strip of all leading or trailing spaces
# use the lower function to convert the string to lower case and assign it to Dow_lower variable
# all inoput values eneterd by the user will be in all lower case
Dow_lower = Dow.strip().lower()


# if, elif, else statements used to check the value of Dow_lower and prints the appropriate message to the terminal
if Dow_lower == "saturday":
    print("Wake up at 9 am")
elif Dow_lower == "sunday":
    print("Wake up at 10 am")
else:
    print("Wake up at 7 am")


