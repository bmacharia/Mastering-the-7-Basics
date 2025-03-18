'''
Write a function, header, that takes a string text and a single character surrond as parameters

Example:

header("Hello, World!", "*"

Output:
*************
Hello, World!
************

header("Python Rocks!", "!")
Output:

!!!!!!!!!!!!!!!
! Python Rocks !
!!!!!!!!!!!!!!!

header("Coders 4 EVER", "+")
Output:
+++++++++++++++++
+ Coders 4 EVER +
+++++++++++++++++


'''

'''
string = "Hello, World!"
print("*" * (len(string) + 4))
print("*", string, "*")
print("*" * (len(string) + 4))'
'''

''''
string = "Hello, World!"
char = "*"
print(char * (len(string) + 4))
print(char, string, char)
print(char * (len(string) + 4))'
'''''


def header(text, surrond):
    print(surrond * (len(text) + 4))
    print(surrond, text, surrond)
    print(surrond * (len(text) + 4))  

def main():
     header("Hello, World!", "*")
     header("Python Rocks!", "!")
     header("Coders 4 EVER", "+")

main()