splitter_dictionary = {}
rays = {}
with open("Input.txt") as file:
    for y, line in enumerate(file):
        line = line.strip()
        for x, character in enumerate(line):
            if character == "S":
                rays[(x,y)] = 1
            elif character == "^":
                splitter_dictionary[(x,y)] = 1
            
    depth = y
    
for i in range(depth):
    next_rays = {}
    for ray_pos,count in rays.items():
        ray_x,ray_y = ray_pos
        new_y = ray_y + 1
        if (ray_x,new_y) in splitter_dictionary:
            if (ray_x-1,new_y) in next_rays:
                next_rays[(ray_x-1,new_y)] += count
            else:
                next_rays[(ray_x-1,new_y)] = count
                
            if (ray_x+1,new_y) in next_rays:
                next_rays[(ray_x+1,new_y)] += count
            else:
                next_rays[(ray_x+1,new_y)] = count
        else:
            if (ray_x,new_y) in next_rays:
                next_rays[(ray_x,new_y)] += count
            else:
                next_rays[(ray_x,new_y)] = count
            
        
    rays = next_rays
    
print(sum(rays.values()))