total = 0
count = 0

# First number
num = float(input("Enter first number: "))
total += num
count += 1

# Second number
num = float(input("Enter second number: "))
total += num
count += 1

while True:
    choice = input("Do you want to enter another number? (yes/no): ").lower()

    if choice == "no":
        break

    num = float(input("Enter another number: "))
    total += num
    count += 1

average = total / count

print("Average =", average)
