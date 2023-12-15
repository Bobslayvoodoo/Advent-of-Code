with open("Input.txt") as file:
    Sequence = file.readline().strip().split(",")

Total = 0
for S in Sequence:
    Current = 0
    for Character in S:
        Code = ord(Character)
        Current += Code
        Current *= 17
        Current = Current % 256
    Total += Current

print(Total)
