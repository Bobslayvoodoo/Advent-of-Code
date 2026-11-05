class RedTile:
    def __init__(self,pos):
        self.x = int(pos[0])
        self.y = int(pos[1])
        
class GreenTileLine:
    def __init__(self,start_tile,end_tile):
        self.start_tile = start_tile
        self.end_tile = end_tile
        x_diff = self.end_tile.x - self.start_tile.x
        if x_diff != 0:
            self.length = abs(x_diff)
            self.orientation = "horizontal"
        else:
            self.length = abs(self.end_tile.y - self.start_tile.y)
            self.orientation = "vertical"
        
    def is_pos_on_line(self,pos):
        if self.orientation == "horizontal":
            if pos[1] == self.start_tile.y:
                if min(self.start_tile.x,self.end_tile.x) <= pos[0] <= max(self.start_tile.x,self.end_tile.x):
                    return True
            return False
        else:
            if pos[0] == self.start_tile.x:
                if min(self.start_tile.y,self.end_tile.y) <= pos[1] <= max(self.start_tile.y,self.end_tile.y):
                    return True
            return False
        
        
    # properly in not just scraping the boundry
    def is_in_square(self,corner1,corner2):
        box_start_x = min(corner1.x,corner2.x)
        box_end_x = max(corner1.x,corner2.x)
        
        box_start_y = min(corner1.y,corner2.y)
        box_end_y = max(corner1.y,corner2.y)
        
        line_start_x = min(self.start_tile.x,self.end_tile.x)
        line_end_x = max(self.start_tile.x,self.end_tile.x)
        
        line_start_y = min(self.start_tile.y,self.end_tile.y)
        line_end_y = max(self.start_tile.y,self.end_tile.y)
        
        if self.orientation == "vertical":
            
            if line_start_x <= box_start_x or box_end_x <= line_start_x:
                return False

            if line_start_y < box_start_y and box_start_y < line_end_y:
                return True
            if line_start_y < box_end_y and box_end_y < line_end_y:
                return True
        
            if box_start_y <= line_start_y and line_end_y <= box_end_y:
                return True
            
        else:
            if line_start_y <= box_start_y or box_end_y <= line_start_y:
                return False

            if line_start_x < box_start_x and box_start_x < line_end_x:
                return True
            if line_start_x < box_end_x and box_end_x < line_end_x:
                return True
        
            if box_start_x <= line_start_x and line_end_x <= box_end_x:
                return True
        
checked = {}
def is_pos_inside(position):
    # is it bang on the line?
    for line in green_lines:
        if line.is_pos_on_line(position):
            #checked[position] = True
            return True
    
    # is it inside the lines?
    cross_count = 0
    for line in green_lines:
        if line.orientation == "horizontal":
            continue
        
        if min(line.start_tile.y,line.end_tile.y) <= position[1] < max(line.start_tile.y,line.end_tile.y):
            if line.start_tile.x < position[0]:
                cross_count += 1
        
    if cross_count % 2 == 0:
        #checked[position] = False
        return False
    else:
        #checked[position] = True
        return True
    
red_tiles = []
green_lines = []

with open("Input.txt") as file:
    for pos, line in enumerate(file):
        new_tile = RedTile(line.strip().split(","))
        red_tiles.append(new_tile)
        if pos == 0:
            continue
        
        new_line = GreenTileLine(red_tiles[-2],new_tile)
        green_lines.append(new_line)
        
    new_line = GreenTileLine(red_tiles[-1],red_tiles[0])
    green_lines.append(new_line)
    
            
all_possible_squares = []
for a,red_tile_1 in enumerate(red_tiles):
    for red_tile_2 in red_tiles[a+1:]:
        x_diff = abs(red_tile_1.x - red_tile_2.x) + 1
        y_diff = abs(red_tile_1.y - red_tile_2.y) + 1 
        size = x_diff*y_diff
        all_possible_squares.append((size,red_tile_1,red_tile_2))
        
all_possible_squares.sort(reverse=True,key=lambda a:a[0])
print("This might take a little while... ")
for progress, possible_square in enumerate(all_possible_squares):
    bad_square = False
    corner1 = possible_square[1]
    corner2 = possible_square[2]
    middle_x = (corner1.x + corner2.x) // 2
    middle_y = (corner1.y + corner2.y) // 2
    quick_checks = [(middle_x,middle_y),(corner1.x,middle_y),(corner2.x,middle_y),(middle_x,corner1.y),(middle_x,corner2.y),
                    (corner2.x,corner1.y),((corner1.x,corner2.y))]
    for pos in quick_checks:
        if not is_pos_inside(pos):
            bad_square = True
            break
    if bad_square == True:
        continue
    
    # if a line is in the area, and not in on the edge of box, then it has to be invalid right? YES
    for line in green_lines:
        if line.is_in_square(corner1,corner2):
            bad_square = True
            break
            
    if bad_square == True:
        continue
    
    ## full check that after thinking about it, is completely unrealistic given the numbers we are working with 
#     for check_y in range(min(corner1.y,corner2.y),max((corner1.y,corner2.y))+1):
#         if bad_square == True:
#             break
# 
#         for check_x in range(min(corner1.x,corner2.x),max((corner1.x,corner2.x))+1):
#             pos = (check_x,check_y)
#             if is_pos_inside(pos):
#                 continue
#             else:
#                 bad_square = True
#                 break
    if bad_square == False:
        print(possible_square[0])
        break
    