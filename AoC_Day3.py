with open('/home/y0ooo0/Documents/AoC.txt', "r") as file:
    input = file.readlines()

wire1 = input[0].split(',')
wire2 = input[1].split(',')

intersection = []

def pathing(wire):
    path = set()
    x, y = 0, 0
    for i in wire:
        inc, count = 0, 0
        units = int(i[-(len(i) - 1):])
        while count != units:
            if i[inc] == 'R':     
                x = x + 1                                                  
            elif i[inc] == 'L':   
                x = x - 1                                           
            elif i[inc] == 'U':     
                y = y + 1                       
            elif i[inc] == 'D':         
                y = y - 1  
            path.add((x, y))              
            count = count + 1
    return path

wire1_path = pathing(wire1)
wire2_path = pathing(wire2)

intersection = set(wire1_path) & set(wire2_path)

smallest = 10000000

for coord in intersection:
    if abs(coord[0]) + abs(coord[1]) < smallest:
        smallest = abs(coord[0]) + abs(coord[1])

print (smallest)