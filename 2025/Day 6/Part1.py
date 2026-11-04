inputs = []
operators = []
with open("Input.txt") as file:
    for line in file:
        line = line.strip().split(" ")
        column_number = 0
        for number in line:
            if number.isnumeric():
                if len(inputs) <= column_number:
                    inputs.append([])
                inputs[column_number].append(int(number))
                column_number += 1
            elif number != "":
                operators.append(number)
                
grand_total = 0
for column_number,operands in enumerate(inputs):
    total = 0
    operator = operators[column_number]
    for number in operands:
        if total == 0:
            total = number
            continue
        if operator == "*":
            total *= number
        elif operator == "+":
            total += number
    grand_total += total
                
print(grand_total)
        