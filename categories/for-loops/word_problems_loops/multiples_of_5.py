for i in range (10,30,5):
    print(i, end=" ")
print()


for i in range (-3,21,3):
    print(i, end=", ")
print()


def calculate_average():
    
    '''The total variable will hold the sum of the 10 numbers entered by the user'''
    total = 0.0
    '''I will use a for loop using range to prompt the user for 10 numbers and those numbers are stored in the total variable'''
    for i in range(10):
        user_numbers = input("Enter a number: ")
        total += float(user_numbers)
    '''The average is calculated by taking the total and dividing it by to'''
    average = total / 10
    '''The average is returned'''
    print("The average of the ten numbers is: ", average)
  
    
    
    
calculate_average()