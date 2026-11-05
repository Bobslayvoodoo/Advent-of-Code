red_tile_locations = []
with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(",")
        x = int(line[0])
        y = int(line[1])
        red_tile_locations.append((x,y))
        
        
biggest = 0
for red_tile_1 in red_tile_locations:
    for red_tile_2 in red_tile_locations:
        if red_tile_1 == red_tile_2:
            continue
        
        x_diff = abs(red_tile_1[0] - red_tile_2[0]) + 1
        y_diff = abs(red_tile_1[1] - red_tile_2[1]) + 1 
        size = x_diff*y_diff
        if size > biggest:
            biggest = size
            
print(biggest)
