
import math

def factorial(n):
    fact = 1
    for x in range(1,n+1):
        fact = fact * x

    return fact

def calculate_binomi(n, k):
    if k == 1 or k == n:
        print(1)

    if k > n:
        return False
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        div = a // (b*(n-k))
        return div


value1 = int(input("Anna ensimmäinen luku "))
value2 = int(input("Anna toinen luku "))


print("Luvun 1 factorial on: ", factorial(value1))
print("The value of n choose k: ", calculate_binomi(value1, value2)) 



      
