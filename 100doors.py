def doorChange(x, y, doors):
    for door in range(x, len(doors), y):
        if doors[door] == 'Open':
            doors[door] = 'Closed'
        elif doors[door] == 'Closed':
            doors[door]= 'Open'
    return doors

#---SAMPLE CASE---#
# doors = ['open', 'Closed', 'Open', 'Closed']
# i = 0
# x = 1
# doors = ['Open' if doors[book] == 'Closed' else doors[book] for book in range(i, len(doors), x)]
# print(doors)
#---SAMPLE CASE ---#

doors = ['Open'] * 100
# #Go through doors and open every second door
# print(doors)
#This code works for the increments we need. Need to make '2' and '3' variables that into the for loop
# for book in range(2, len(doors), 3):
#     if doors[book] == 'Open':
#         doors[book] = 'Closed'
x = 1
y = 2
while x < len(doors):
    doors = doorChange(x, y, doors)
    x += 1
    y += 1

for num, door in enumerate(doors, start=1):
    if door == 'Open':
        print("Door {} is open".format(num))

#Old and broken code:
# i = 1
# while i < 4:
#     print(i)
#     for x in doors:
#         if x == 'Closed':
#             x = 'Open'
#     i += 2
# print(doors)

#Could turn this into a function???
# for book in range(i, len(doors), i):
#     if doors[book] == 'Closed':
#         doors[book] = 'Open'
#     print(doors[book])
#List comprehension of the above:
# doors = ['Open' for book in range(i, len(doors), i) if doors[book] == 'Closed']