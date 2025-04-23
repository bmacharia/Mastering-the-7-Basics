i = 1
while i <= 5:
    print(i)
    i += 1
print("All done with this")


# intializing the variable
# set the loop counter to -10 as it is the first number to be printed
i = -10
# Test th condition
while i <= 0:
    # print the current value of i, then a space to keep on same line
    print(i, end=" ")
    # decrement i by 2, since we are added to a negative number
    # this will print the next negative number
    i += 2
print()


i = 2
while i <= 11:
    print(i)
    i += 3
print()

i = 1
while i <= 4:
    print("*" * 4)
    i += 1

""""
intializing the variable
text = "CSCI 150"

# Test the condition
while i is less the the length of the text:

# Execute the body
print the first value of the test

# update the counter to move the index to the next letter inthe sequence 
i += 1  

# Loop exit

when i == len(text) the condition fails and the loop ends

"""


TEXT = "CSCI 150"
i = 0
while i < len(TEXT):
    print(TEXT[i])
    i += 1


# ————————————————————————————————————————————————
# 1. Initialize an empty list to hold user inputs
numbers = []

# 2. Keep asking until the user enters 0
while True:
    num = float(input("Enter a number (0 to finish): "))
    if num == 0:
        break  # 3. Exit loop when 0 is entered
    numbers.append(num)  # 4. Otherwise, add the number to our list

# 5. Sort the list in ascending order
numbers.sort()

# 6. Compute the sum of all entered numbers
total = sum(numbers)

# 7. Compute the average (guard against division by zero)
average = total / len(numbers) if numbers else 0

# 8. Display results
print("\nSorted numbers:", numbers)
print("Sum:         ", total)
print("Average:     ", average)


def average_neg_evens(nums):
    for num in nums:
        if num < 0 and num % 2 == 0:
            print(num)
    return num


# Example usage
numbers = [1, -2, 3, -4, 5, -6]
result = average_neg_evens(numbers)
print("Average of negative even numbers:", result)


"""
    count_letter funtion
    this function will take in a list of strings and a letter as parameters
    the count_letter function will return the number of times the letter appears
    in the lsit of string values.  
    the letter can be upper case or lower case 

    list = ["HELLO", "goodbye", "1234 Oooh!"]
    print(count_letter(list, "o"))

    Outputs 6


"""


def count_letter(lst, char):
    total = 0  # 1. Start with zero occurrences
    lower_char = char.lower()  # 2. Normalize the search letter to lowercase
    for string in lst:  # 3. Loop over each string in the list
        total += string.lower().count(lower_char)
        #    a. Convert the string to lowercase
        #    b. count() returns how many times lower_char appears
        #    c. add that count to total
    return total  # 4. After the loop, return the total count


# Example usage
list_of_strings = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list_of_strings, "o"))  # Outputs 6
