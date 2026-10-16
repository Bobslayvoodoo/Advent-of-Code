class Dial:
    def __init__(self):
        self._rotation = 50
        
    def rotate(self,command):
        if not command.isalnum():
            return
        if command[0] == "R":
            mult = 1
        elif command[0] == "L":
            mult = -1
        else:
            return
        
        if not command[1:].isnumeric():
            return
        
        amount = int(command[1:]) * mult
        new_rotation = (amount + self._rotation) % 100
        self._rotation = new_rotation
        
    def get_rotation(self):
        return self._rotation
    
    
dial = Dial()
total = 0
with open("Input.txt") as file:
    for line in file:
        line = line.strip()
        dial.rotate(line)
        if dial.get_rotation() == 0:
            total += 1
            
print(total)
        