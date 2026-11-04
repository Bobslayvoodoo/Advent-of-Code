inputs = []
operators = []

with open("Input.txt") as file:
    for line in file:
        line = line.strip("\n")
        for column_number, character in enumerate(line):
            if character in "*+":
                operators.append(character)
                continue
            if len(inputs) <= column_number:
                inputs.append([])
            inputs[column_number].append(character)
    
grand_total = 0
total = 0
operator_number = 0
for digits in inputs:
    
    operator = operators[operator_number]
    
    number = "".join(digits).strip()
    if number == "":
        grand_total += total
        total = 0
        operator_number += 1
        continue
    number = int(number)
    if total == 0:
        total = number
        continue
    if operator == "*":
        total *= number
    elif operator == "+":
        total += number
        
grand_total += total

print(grand_total)
        