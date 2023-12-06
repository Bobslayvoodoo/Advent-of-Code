replacements = {
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"}

def FindLetterNum(txt):
    for Val in replacements.keys():
        location = txt.find(Val)
        if location > -1:
            return location, len(Val)
    return -1, 0

with open("input.txt") as file:
    Total = 0
    for line in file:
        line = line.strip()
        n=0
        Current = line[n]
        while Current.isalpha():
            n += 1
            Current = line[n]
            Location,L = FindLetterNum(line[:n+1])
            if  Location > -1:
                Current = replacements[line[Location:n+1]]
        First = Current
        
        n=len(line) -1
        Current = line[n]
        while Current.isalpha():
            n -= 1
            Current = line[n]
            Location,L = FindLetterNum(line[n:])
            if  Location > -1:
                Current = replacements[line[n:n+L]]
        Second = Current
        Combined = int(First+Second)
        Total += Combined
print(Total)
