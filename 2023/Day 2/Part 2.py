

Total = 0
with open("Input.txt") as file:
    for line in file:
        RedMin = 0
        GreenMin = 0
        BlueMin = 0

        Cubes = {
            "red":RedMin,
            "green":GreenMin,
            "blue":BlueMin}
        
        data = line.split(":")[1]
        for CubeSet in data.split(";"):
            for Cube in CubeSet.split(","):
                Cube = Cube.strip()
                Number = int(Cube.split(" ")[0])
                Colour = Cube.split(" ")[1]
                if Number > Cubes[Colour]:
                    Cubes[Colour] = Number
        Power = Cubes["red"] * Cubes["green"] * Cubes["blue"]
        Total += Power

print(Total)
        
