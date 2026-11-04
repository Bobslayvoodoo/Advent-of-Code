WANTED_CONNECTIONS = 1000


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

successful_connections = 0
while successful_connections < WANTED_CONNECTIONS:
    current_box = sorted_boxes[0]
    current_box.connect_to_closest()
    #print("connected",current_box,"to",current_box.closest)
    sorted_boxes.sort(key=lambda b: b.distances[0][0])
    successful_connections += 1
    
circuit_sizes = []
while len(junction_boxes) > 0:
    start_box = junction_boxes.pop(0)
    explored = [start_box]
    queue = list(start_box.connections)
    while len(queue) > 0:
        current_box = queue.pop(0)
        if current_box in explored:
            continue
        junction_boxes.remove(current_box)
        explored.append(current_box)
        queue += current_box.connections
    circuit_sizes.append(len(explored))
    
circuit_sizes.sort(reverse=True)
# whole thing feels messy but it works
print(circuit_sizes[0]*circuit_sizes[1]*circuit_sizes[2])
    
    
    
    
    
    
    
    
    
    