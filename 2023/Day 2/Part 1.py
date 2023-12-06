RedMax = 12
GreenMax = 13
BlueMax = 14

Cubes = {
    "red":RedMax,
    "green":GreenMax,
    "blue":BlueMax}

Total = 0
with open("Input.txt") as file:
    for line in file:
        ID = int(line.split(":")[0].split(" ")[1])
        data = line.split(":")[1]
        Works = True
        for CubeSet in data.split(";"):
            for Cube in CubeSet.split(","):
                Cube = Cube.strip()
                Number = int(Cube.split(" ")[0])
                Colour = Cube.split(" ")[1]
                if Number > Cubes[Colour]:
                    Works = False
        if Works == True:
            Total += ID

print(Total)
        
