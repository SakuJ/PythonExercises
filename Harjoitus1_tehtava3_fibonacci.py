
kerrat = 4

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

for i in range(5):
       print(fibonacci(i), end = ' ')
print("\n")
if kerrat >= 10:
    for i in range(5,10):
       print(fibonacci(i), end = ' ')
print("\n")
if kerrat >= 15:
    for i in range(10,kerrat):
       print(fibonacci(i), end = ' ')
