def doorChange(x, y, doors):
    for door in range(x, len(doors), y):
        if doors[door] == 'Open':
            doors[door] = 'Closed'
        elif doors[door] == 'Closed':
            doors[door]= 'Open'
    return doors


doors = ['Open'] * 100
x = 1
y = 2
while x < len(doors):
    doors = doorChange(x, y, doors)
    x += 1
    y += 1

for num, door in enumerate(doors, start=1):
    if door == 'Open':
        print("Door {} is open".format(num))

