with open("input.txt") as file:
    Total = 0
    for line in file:
        line = line.strip()
        n=0
        Current = line[n]
        while Current.isalpha():
            n += 1
            Current = line[n]
        First = Current
        n=len(line) -1
        Current = line[n]
        while Current.isalpha():
            n -= 1
            Current = line[n]
        Second = Current
        Combined = int(First+Second)
        Total += Combined
print(Total)
