### Part Four -- your code goes here. 
import random

a = 10
list = []
for x in range(a):
  list.append(random.randint(1, 100))
  list.sort()

amount = 0

while amount < len(list):
  if list[amount] % 2 == 0:
    list.pop(amount)
  else:
    amount += 1

print(list)