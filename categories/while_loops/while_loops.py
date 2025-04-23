"""
j = 4
while j > -4:
    print(j)
    j -= 1
"""

'''
# declare a a varible named string with the value "Hello"
string = "Hello"
# declare an empyt string named builder and assign it to the empty string
builder = ""
# declare a variable named i and assign it to 0
i = 0
# the while loop will run as long as the value of i is less than the lenght of the string
while i < len(string):
    """
    iterate over the string value at index i, call the function swapcase on each value of the string and add the result to the builder variable
    swapcase will change the case of the string value at index i, if the value is lower case it will be changed to upper case and if the value is upper case it will be changed to lower case

    """
    builder += string[i].swapcase()
    print(i, builder)
    i += 1
print(string, "-->", builder)
'''


x = 0
i = 1
while x < 20:
    if x > 5:
        x += 15
    else:
        x += 1
print(i, x)
i += 1


string = "HELLO"
x = 0
while string[x] != "L":
    print(string[x], end="...")
    x += 1
print("\n", string, "first L is at", x)


list = []
prompt = "Please enter a word, 'done' to finish"
response = input(prompt)
while response != "done":
    list.append(response)
    response = input(prompt)
print(sorted)
