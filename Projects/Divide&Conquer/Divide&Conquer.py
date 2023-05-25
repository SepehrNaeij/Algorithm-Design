import math

# Some information about the 'multiply' function:
# This function calculate the product of two numbers with using from 'Divide and Conquer' method.
# This function is the type of a Recursive Function.
# This function can calculate the product of the numbers which have more than 8 number.
# This function caculate the product of numbers's parts first and at last caculate the sum of all parts,The return the value of it.

def multiply(x, y):  
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        size = n // 2

        a = x // 10**(size)
        b = x % 10**(size)
        c = y // 10**(size)
        d = y % 10**(size)

        ac = multiply(a, c)
        bd = multiply(b, d)
        ad_plus_bc = multiply(a+b, c+d) - ac - bd

        # this little trick, writing n as 2*size takes care of both even and odd n
        product = ac * 10**(2*size) + (ad_plus_bc * 10**size) + bd

        return product

# This function caculate the pow of the first_number to last_number and return it.
def main_result(x,y):
    a = str(multiply(x,y))
    length = len(a)
    
    # For achiving to the first and last number.
    first_number = a[0]
    last_number = a[length-1]
    
    number = math.pow(int(first_number),int(last_number))
    
    # Here we did this for removing the '.0' from our result.
    # For example the number 64.0 convert to 64 with this job.
    test = str(number)
    result = test.split(".")
    
    return result[0]


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(str(a) + " * " + str(b) + " = " + main_result(a,b))

