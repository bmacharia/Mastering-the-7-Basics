# Fun with Conditions
# Babu 3/5/20025

x = 3 
y = 7


#print( not x == 5 ) # True
#print(x > 0 and y < 0) # False both conditions must be true
#print(x < 0 or y < 0 )# False only one condition must be true, both conditons are false
#print(x*y > 20 or x*y < -20) # True


# negate the whole expressin which is using an equality operator
print(not ( x == 0 or y == 5))
# this is not the same as the above expression the expression below evaluates to True
print(not x == 0 or y == 5)
print( x == 3 and not y == 5)
print(not ( x == 3 and y == 5))