n = int(input("n: "))

total = 1
while n > 0:
    total *= n
    n = n - 1

print(f"The factorial of {n} is {total}")