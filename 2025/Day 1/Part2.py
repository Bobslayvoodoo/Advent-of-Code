class Dial:
    def __init__(self,target_pos):
        self._rotation = 50
        self._target_pos = target_pos
        self._target_count = 0
        
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
        
        amount = int(command[1:])
        new_rotation = self._rotation
        for click in range(amount):
            new_rotation += mult
            if new_rotation < 0:
                new_rotation = 99
            if new_rotation > 99:
                new_rotation = 0
            if new_rotation == self._target_pos:
                self._target_count += 1
        self._rotation = new_rotation
        
    def get_rotation(self):
        return self._rotation
    
    def get_target_count(self):
        return self._target_count
    
    
dial = Dial(0)
with open("Input.txt") as file:
    for line in file:
        line = line.strip()
        dial.rotate(line)
    print(dial.get_target_count())
        
            
        