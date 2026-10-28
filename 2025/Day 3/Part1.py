total = 0

with open("Input.txt") as file:
    for bank in file:
        bank=bank.strip()
        # get biggest left most numberrr
        first_pointer = len(bank) - 2
        biggest_left_most = 0
        biggest_left_most_pos = -1
        while first_pointer >= 0:
            current_number = int(bank[first_pointer])
            if current_number >= biggest_left_most:
                biggest_left_most = current_number
                biggest_left_most_pos = first_pointer
            first_pointer -= 1
                
        second_pointer = biggest_left_most_pos + 1
        best_second_number = 0
        while second_pointer < len(bank):
            current_number = int(bank[second_pointer])
            if current_number > best_second_number:
                best_second_number = current_number
            second_pointer += 1
            
        joltage = str(biggest_left_most) + str(best_second_number)
        total += int(joltage)
        
print(total)