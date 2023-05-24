# The factorial function gives the number of possible arrangements of a set of items of length "n"

# For example, there are 4! ("four factorial") or 24 ways to arrange four items, which can be calculated as: 4 * 3 * 2 * 1

# 5! = 5 * 4 * 3 * 2 * 1 = 120

# 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

# etc.

# In a set of 0 items (an empty set) there is only one way to arrange the items, therefore, 0! = 1

# For the purposes of this exercise, factorials are only defined for positive integers (including 0)

def getFactorial(number):
    if type(number) is not int:
        return None
    if  number < 0:
        return None
    if number == 0:
        return 1
    
    return number * getFactorial(number - 1)
    

numberFactorial = 5
result = getFactorial(numberFactorial)
print('Factorial of ' + str(numberFactorial) + ' is ' + str(result))