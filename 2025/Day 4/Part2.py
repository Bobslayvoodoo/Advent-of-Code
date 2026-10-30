class Grid:
    def __init__(self,file_name):
        self._grid = []
        with open(file_name) as file:
            for line in file:
                line = line.strip()
                self._grid.append(list(line))
                
        self.width = len(self._grid[0])
        self.height = len(self._grid)
        
    def get_position(self,x,y):
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return
        return self._grid[y][x]
    
    def remove_position(self,x,y):
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return
        self._grid[y][x] = "."
    
    
    
    def count_surrounding(self,x,y):
        deltas = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        count = 0
        for delta in deltas:
            new_x = x + delta[0]
            new_y = y + delta[1]
            if self.get_position(new_x,new_y) == "@":
                count += 1
                
        return count
            
total = 0   
grid = Grid("Input.txt")
removed_rolls = 1
while removed_rolls > 0:
    removed_rolls = 0
    for y in range(grid.height):
        for x in range(grid.width):
            surround_count = grid.count_surrounding(x,y)
            if surround_count < 4 and grid.get_position(x,y)=="@":
                grid.remove_position(x,y)
                removed_rolls += 1
                total += 1

            
print(total)