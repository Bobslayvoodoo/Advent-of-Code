class Lens():
    def __init__(self,Label,FocalLength):
        self.Label = Label
        self.FocalLength = FocalLength


with open("Input.txt") as file:
    Sequence = file.readline().strip().split(",")
Boxes = []
for i in range(256):
    Boxes.append([])

for S in Sequence:
    BoxNumber = 0
    CharPos = 0
    Character = "a"
    Label = []
    Character = S[CharPos]
    while Character.isalpha():
        Code = ord(Character)
        BoxNumber += Code
        BoxNumber *= 17
        BoxNumber = BoxNumber % 256
        Label.append(Character)
        CharPos += 1
        Character = S[CharPos]
        

    Label = "".join(Label)
    CurrentBox = Boxes[BoxNumber]
    if S[CharPos] == "-":
        for Lpos, L in enumerate(CurrentBox):
            if L.Label == Label:
                CurrentBox.pop(Lpos)
                break
        
    elif S[CharPos] == "=":
        FocalLength = int(S.split("=")[1])
        
        for L in CurrentBox:
            if L.Label == Label:
                L.FocalLength = FocalLength
                break
        else:
            NewLens = Lens(Label,FocalLength)
            #print(f"added {S} to {BoxNumber}")
            CurrentBox.append(NewLens)
Total = 0

for Bnum,Box in enumerate(Boxes):
    #print("\n----------")
    #print(Bnum,end="")
    for Snum,L in enumerate(Box):
        #print(L.Label,L.FocalLength,end="")
        FocusingPower = 1+Bnum
        FocusingPower = FocusingPower * (Snum+1) * L.FocalLength
        Total += FocusingPower
        
print(Total)

    
    


