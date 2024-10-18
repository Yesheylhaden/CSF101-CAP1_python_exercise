for i in range (1,6) :
    print(i)

count = 5
while count > 0:
    print(count)
    count -= 1

total = 0
for num in range (1, 11):
    total += num
print(f"The sum of numbers from 1 to 10 is: {total}")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(1,4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")
    print() # Print a newline after each inner loop