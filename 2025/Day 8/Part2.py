
class JunctionBox:
    def __init__(self,pos):
        pos = pos.split(",")
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.z = int(pos[2])
        self.connections = []
        self.distances = []
        
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"
        
    def connect_to_closest(self):
        distance, closest = self.distances.pop(0)
        self.connections.append(closest)
        closest.connections.append(self)
        closest.distances.remove((distance,self))
        
        
junction_boxes = [] 
with open("Input.txt") as file:
    for line in file:
        line = line.strip()
        new_box = JunctionBox(line)
        junction_boxes.append(new_box)
        
for box in junction_boxes:
    closest_distance = float("inf")
    closest_box = None
    for other_box in junction_boxes:
        if box == other_box:
            continue
        distance = ((box.x-other_box.x)**2 + (box.y-other_box.y)**2 + (box.z-other_box.z)**2)**(1/2)
        box.distances.append((distance,other_box))
    box.distances.sort(key=lambda t: t[0])
    
sorted_boxes = sorted(junction_boxes,key=lambda b: b.distances[0][0])
next_test_start = sorted_boxes[-1]
all_connected = False
while all_connected == False:
    test_list = list(sorted_boxes)
    start_box = next_test_start
    test_list.remove(start_box)
    explored = [start_box]
    queue = list(start_box.connections)
    while len(queue) > 0:
        current_box = queue.pop(0)
        if current_box in explored:
            continue
        test_list.remove(current_box)
        explored.append(current_box)
        queue += current_box.connections
        
    if len(test_list) == 0:
        all_connected = True
    else:
        connect_box = sorted_boxes[0]
        connect_box.connect_to_closest()
        sorted_boxes.sort(key=lambda b: b.distances[0][0])
        # make sure we are checking the smallest circuit MASSIVE time save
        if len(test_list) < len(explored):
            next_test_start = test_list[0]
        else:
            next_test_start = explored[0]
    
print(connect_box.x * connect_box.connections[-1].x)
    
    
    
    
    
    
    
    
    
    