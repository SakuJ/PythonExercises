x = int(input("How many number are you going to give?"))
y = 1
sum = 0
for y in range(x):
    luku = int(input("Give a number: "))
    sum = sum + luku
print("Numbers average is: ", sum / x)
