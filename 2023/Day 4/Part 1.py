Total = 0

with open("Input.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(":")
        Numbers = line[1].split("|")
        WinningNumbers = set([""]+Numbers[0].strip().split(" "))
        ElfNumbers = set([""]+Numbers[1].strip().split(" "))
        WinningNumbers.remove("")
        ElfNumbers.remove("")
        #print(WinningNumbers)
        #print(ElfNumbers)
        #print("-------------")
        Points = 1
        for N in ElfNumbers:
            if N in WinningNumbers:
                Points *= 2

        if Points == 1:
            Points = 0
        else:
            Points /= 2
        #print(Points)
        Total += int(Points)

print(Total)
