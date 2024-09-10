sum = 0

for num in range(200, 501):
    if num % 3 == 0:
        sum += num

print("The sum of numbers from 200 to 500 that can be evenly divided by 3 is:", sum)