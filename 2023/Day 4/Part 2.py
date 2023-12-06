
def GetWinnersNum(Line):
    Line = Line.strip()
    Line = Line.split(":")
    Numbers = Line[1].split("|")
    WinningNumbers = set([""]+Numbers[0].strip().split(" "))
    ElfNumbers = set([""]+Numbers[1].strip().split(" "))
    WinningNumbers.remove("")
    ElfNumbers.remove("")
    Winners = 0
    for N in ElfNumbers:
        if N in WinningNumbers and N.isnumeric():
            Winners += 1
    return Winners

print("this will take a while")

Cards = {}
with open("Input.txt") as file:
    limit = 1
    for RowNum,line in enumerate(file):
        CardNum = RowNum + 1
        Cards[CardNum] = line

TotalCards = 0
TotalPointsCheck = 0
Queue = list(range(1,len(Cards)+1))
CompletedOriginals = set()
CardWinsTable = {}
while len(Queue) > 0:
    TotalCards += 1
    CurrentCardNumber = Queue.pop(0)
    #print("-----------")
    #print(CurrentCardNumber)
    CurrentCard = Cards[CurrentCardNumber]
    if CurrentCardNumber in CardWinsTable.keys():
        Winners = CardWinsTable[CurrentCardNumber]
    else:
        CardWinsTable[CurrentCardNumber] = GetWinnersNum(CurrentCard)
        Winners = CardWinsTable[CurrentCardNumber]
        
    if Winners > 0:
        #print("Copy")
        #print(f"{CopiesWon} won")
        Queue += list(range(1+CurrentCardNumber,Winners+CurrentCardNumber+1))
        if not CurrentCardNumber in CompletedOriginals:
            Points = 2**(Winners-1)
            TotalPointsCheck += Points
            CompletedOriginals.add(CurrentCardNumber)    
    
print(TotalPointsCheck)
print(TotalCards)

    
    

        
        


