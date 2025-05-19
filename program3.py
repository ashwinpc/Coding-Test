n = int(input("Enter a number: "))

if n % 2 == 0:
    n -= 1  # Make it odd

for i in range(1, n + 1, 2):
    print(i, end=", ")
