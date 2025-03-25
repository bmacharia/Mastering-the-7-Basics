# Writing Functions
# by Babu


'''

Write a function `is_even` that takes a number as a parameter and returns whether or not it is even. Test that your function works by calling it twice (once with an even number and once with an odd number), and print the results.

To determine if a number is even, it means that the number is divisible by 2 with no remainder. You can use the modulus operator `%` to check this condition.

'''

def calculate_total(meal_cost, tax_rate, tip_rate):
    '''
    this function takes as paraments the cost of the the mealm the tax rate and the tip rate and calcullates the total cost of the meal
    '''
    # to calculate the tax amount, multiply the meal_cost by the tax_rate
    tax_amount = meal_cost * tax_rate
    # to calculate the tip amount, multiply the meal_cost by the tip_rate
    tip_amount = meal_cost * tip_rate
    # to calculate the total cost, add the meal_cost, tax_amount and tip_amount
    total_cost = meal_cost + tax_amount + tip_rate
    # return the total cost
    return total_cost
    



def is_even(number):#
    # this function si#mply takes a number and checks if it is even
    # by checking if t#he remainder when divided by 2 is zero
    # if it is zero, t#hen the number is even
    # otherwise, it is# odd
  return number % 2 #

# this function simply takes a number, squares it, an returns it to the caller
def hey(number):
     return number * number

def are_we(num, phrase):
   # the loop runs num times and prints the phrase
   for i in range(num):
      # the phrase gets printer during each loop iteration num times
      print(phrase)
  

def there(n):
   if n < 0:
      return 
   return 2 ** n   



def main():
  print(is_even(4))  # Should print True, since 4 is even
  print(is_even(5))  # Should print False, since 5 is odd
  print("You owe this much, Pay up or wash dishes", calculate_total(100, 0.08, 0.15))
  print(hey(5))
  print(hey(0))
  print(hey(-3))
  are_we(5, "99 Bottles of Beer on the wall")
  are_we(5, " No we are not there yet!")
  print(there(5))
  print(there(-4))

main()
    