import random
x = 0
n=0
for c in range(1,4):
    x = int(input("Guess a number between 1 and 5."))
    n = random.randint(1,5)
    if x==n:
        print("LUCKY YOU!")
        break
