### Part Three -- your code goes here. 
list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
list = [x for x in list if x != 1]
list.sort()
list.append(7)
list.append(8)
print(list)