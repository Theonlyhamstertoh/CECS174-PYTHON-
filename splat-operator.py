from tkinter import Grid

# grid = []
# for y in range(10):
#     grid.append([])
#     for x in range(10):
#         grid[y].append(y * 10 + x + 1)
#     print(grid[y])

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# The spread operator, loops through each item in list
# Format the spaces to all items in list
frmt = "{:^5}" * len(list)

# {:^5}{:^5}{:^5}....
print(frmt)

# For each format type in string, format it with every item in list
print(frmt.format(*list))


