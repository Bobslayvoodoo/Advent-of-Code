splitter_dictionary = {}
rays = set()
with open("Input.txt") as file:
    for y, line in enumerate(file):
        line = line.strip()
        for x, character in enumerate(line):
            if character == "S":
                rays.add((x,y))
            elif character == "^":
                splitter_dictionary[(x,y)] = 1
            
    depth = y
    
split_count = 0
for i in range(depth):
    next_rays = set()
    for ray in rays:
        ray_x,ray_y = ray
        new_y = ray_y + 1
        if (ray_x,new_y) in splitter_dictionary:
            next_rays.add((ray_x-1,new_y))
            next_rays.add((ray_x+1,new_y))
            split_count += 1
        else:
            next_rays.add((ray_x,new_y))
        
    rays = next_rays
    
print(split_count)