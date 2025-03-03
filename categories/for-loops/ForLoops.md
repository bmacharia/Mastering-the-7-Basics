# Why Loops, Less is More

## Print the numbers from 1 to 10

The Long Way

```python
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

```

Below is an example of using a for loop

```python
   # Example Print 1 to 10

   for i in range (1, 11):
     # print(i) is the repeated code
     # the print() is called on each iteration
     print(i)

```

### For Loop Template

```
for <loop variable> in <sequence>:
  # do repeated code
```

### Example: String For Loop

At every iteratin of the lop, the loop variable char is getting its next value in the sequence "hello"
The string "hello" is a sequence of characters

```python
  for char in "hello":
    print(char)
```

### The Range Function

The below code prints the sequence **0, 1, 2 ,3**

```python
    for i in range(4)
      print(i)
```

```python
    range(0)
---> include 0 [0, x)<---- exclude 4

```
