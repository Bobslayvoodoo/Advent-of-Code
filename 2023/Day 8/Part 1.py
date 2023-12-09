class Node():
    def __init__(self,Name,Left,Right):
        self.Name = Name
        self.Left = Left
        self.Right = Right


Network = dict()
with open("Input.txt") as File:
    for Row,Line in enumerate(File):
        if Row == 0:
            Directions = Line.strip()
        elif Row >= 2:
            Line = Line.strip().split("=")
            Key = Line[0].strip()
            D = Line[1][2:-1].split(",")
            Left = D[0].strip()
            Right = D[1].strip()
            NewNode = Node(Key,Left,Right)
            Network[Key] = NewNode

for N in Network.values():
    N.Left = Network[N.Left]
    N.Right = Network[N.Right]

CurrentNode = Network["AAA"]
Steps = 0
while CurrentNode.Name != "ZZZ":
    Steps += 1
    Dnum = (Steps-1) % len(Directions)
    Direction = Directions[Dnum]
    if Direction == "L":
        CurrentNode = CurrentNode.Left
    elif Direction == "R":
        CurrentNode = CurrentNode.Right
    else:
        print("Something has gone wrong")

print(Steps)
            
