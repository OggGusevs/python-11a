width = 10
height = 5  

for i in range(height):
    print('*' * width)

side = 5

for i in range(side):
    print('*' * side)

levels = 5 

for i in range(1, levels + 1):
    spaces = ' ' * (levels - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
