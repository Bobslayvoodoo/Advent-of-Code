
Times = []
Distances = []

with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(":")
        if line[0] == "Time":
            for time in line[1].strip().split(" "):
                if time.isnumeric():
                    Times.append(int(time))
        elif line[0] == "Distance":
            for Dist in line[1].strip().split(" "):
                if Dist.isnumeric():
                    Distances.append(int(Dist))

Total = 1
for RaceNum in range(len(Times)):
    HoldTime = 1
    Wins = 0
    while HoldTime < Times[RaceNum]-1:
        DistanceTravelled = HoldTime * (Times[RaceNum]-HoldTime)
        if DistanceTravelled > Distances[RaceNum]:
            Wins += 1
        HoldTime += 1
    Total *= Wins


print(Total)

