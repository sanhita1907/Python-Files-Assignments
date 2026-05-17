num = int(input("Enter a 2-digit number: "))

first = num // 10
second = num % 10

if first == second:
    print(f"{num} is a PALINDROME")
else:
    print(f"{num} is NOT a palindrome")
