Strengths = {
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14}

def GetStrength(Card):
    if Card.isnumeric():
        return int(Card)
    else:
        return Strengths[Card]

def GetType(Hand):
    Uniques = {}
    for Card in Hand:
        if Card in Uniques.keys():
            Uniques[Card] += 1
        else:
            Uniques[Card] = 1
    if len(Uniques) == 5: # high card
        return 0 
    elif len(Uniques) == 4: # One pair
        return 1 
    elif len(Uniques) == 3:
        if max(Uniques.values()) == 2: # Two pair
            return 2
        else: # Three of a kind
            return 3
    elif len(Uniques) == 2:
        if max(Uniques.values()) == 3: # full house
            return 4
        else: # Four of a kind
            return 5
    elif len(Uniques) == 1: # Five of a kind
        return 6
    else:
        print("Something has gone wrong")
        
def CompareHands(HandA,HandB):
    HandAType = GetType(HandA)
    HandBType = GetType(HandB)
    if HandAType > HandBType:
        return HandA
    elif HandBType > HandAType:
        return HandB

    for CurrentCardNum in range(len(HandA)):
        CardA = HandA[CurrentCardNum]
        CardB = HandB[CurrentCardNum]
        StrengthA = GetStrength(CardA)
        StrengthB = GetStrength(CardB)
        if StrengthA > StrengthB:
            return HandA,HandB
        elif StrengthB > StrengthA:
            return HandB,HandA

AllHands = {}

with open("Input.txt") as file:
    Batches = {}
    for Line in file:
        Line = Line.strip().split(" ")
        Hand = Line[0]
        Bid = int(Line[1])
        HandType = GetType(Hand)
        AllHands[Hand] = Bid
        if HandType in Batches.keys():
            Batches[HandType][Hand] = Bid
        else:
            Batches[HandType] = {}
            Batches[HandType][Hand] = Bid

SortedEntries = []
for BatchNumber in range(6,-1,-1):
    if not BatchNumber in Batches.keys():
        continue
    CurrentBatch = list(Batches[BatchNumber].keys())
    ChangeMade = True
    
    while ChangeMade == True:
        CurrentPos = 0
        ChangeMade = False
        while CurrentPos < len(CurrentBatch)-1:
            Higher,Lower = CompareHands(CurrentBatch[CurrentPos],CurrentBatch[CurrentPos+1])
            if Lower == CurrentBatch[CurrentPos]:
                ChangeMade = True
            CurrentBatch[CurrentPos] = Higher
            CurrentBatch[CurrentPos+1] = Lower
            CurrentPos += 1
    SortedEntries.append(CurrentBatch)

TotalWinnings = 0
Rank = len(AllHands)
for CurrentBatch in SortedEntries:
    for Hand in CurrentBatch:
        Bid = AllHands[Hand]
        Winnings = Rank * Bid
        #print(f"{Rank} * {Bid}")
        TotalWinnings += Winnings
        Rank -= 1

print(TotalWinnings)
    
    
            
