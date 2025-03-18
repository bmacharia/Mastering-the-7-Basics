# Writing your own Functions

Writing functions unlocks the true power of programming. A function is a named block of statements that can be called with input parameters. It is not necessary for a fucntion to have input parameters to be called a function, it just has to be a named block of statements

The key to writing fucntions is identifying what is always the same versus what will vary.

## Example Problem

Write a fucntion,**header** that takes as input a **string text** and a single character **surround** as parameters and displays the following

```python

# Example Call

header("Hello, World!", "*")

# The outpout of this function will be

*****************
* Hello, World! *
*****************

header("Python Rocks", "!")

# The output of this function will be

!!!!!!!!!!!!!!!!
! Python Rocks !
!!!!!!!!!!!!!!!

header("Coders 4 EVER", "+")

+++++++++++++++++
+ Coders 4 EVER +
++++++++++++++++


```

#### Steps to Implement

Begin with an example. Write the lines of code to output the example test cases.

```python
string = ("Hello, World!") # text to disply in the console
print("*" * (len(string) + # display the top line **************
print("*" , string, "*")   # display the middle line
print("*", * len(string) + 4)) # dispkay the bottom line

```

### Test the Code

Run the code to ensure that the output matched the target example

### Make variable for repeated values

If there are any values in the example code solution that are repeated, replace them with variable. In the example above the string "Hello World" and the "\*" character are used multiple times

```python

string = "Hello, World!" # text to display
char = "*"  the character that will surround the text
print(char * (len(string) + 4) # display the top line
print(char, string, char)  # display the middle line
print(char * (len(string) + 4) # display the bottome line
```

### Identify the Parameters

Of th e variable that I created, which will stay the same & which will vary when I want to call the function with a different set of parameters. The variables that I expect to change will become the parameters.
In the example what changes is the text to display and the character that will surround the text

### Write a function signature

Now at this point I can define the first line of the function.

From the example problem statement

_Write_ a function, **header**, that takes a string text and a single character surround as parameters

From this the function signature is as the following

```python

def header(text, surround):

```

### Substitute in parameters

```python

def header(text, surround):
  print(surround * (len(text) + 4 )) # display the top
  print(surround, text surround) # display the middle line
  print(surround * (len(text) + 4) 0 # display the bottom  line
```

### Test the function

Now it is time to text the generalizabilty and resuabilty of the function -- does it work correctly with parameters other than the original test case? The output should match the example output exactly. If it does not, refine the implementation until it does

## Function Writing Checklist

1.  **Understand what to implement** begin with a test case
2.  **Test the code**: run the code to ensure that the output matches the target example test case
3.  **Make variables for repeated values**: Any values in the code that repeat, replace with variables
4.  **Identify the Parameters**: The variables that I expect to change when the function is called will become the parameters
5.  **Write Function Signature**: define the first line of the function
6.  **Substitute in Parameters**: Finish implementing the function's body by changing the variables over to parametersby identifying which variables shoukd become which parametes and aliging the names to match
7.  **Test the function**: test the function by calling it from main, with the same test case
8.  **Test the function**; test the function by using parameters other than from the example test case. If the output does not match, refine the implementation
