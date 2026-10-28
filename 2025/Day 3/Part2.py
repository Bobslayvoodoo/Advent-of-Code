total = 0
required_batteries = 12



with open("Input.txt") as file:
    for bank in file:
        bank=bank.strip()
        
        selected_batteries = []
        previous_point = -1
        while len(selected_batteries) < required_batteries:
            # leave room for the other batteries i need
            pointer = len(bank) - (required_batteries - len(selected_batteries))
            current_best = 0
            current_best_point = 0
            while pointer > previous_point:
                current = int(bank[pointer])
                if current >= current_best:
                    current_best_point = pointer
                    current_best = current
                pointer -= 1
            selected_batteries.append(str(current_best))
            previous_point = current_best_point
                    
            
            
        
            
        joltage = "".join(selected_batteries)
        total += int(joltage)
        
print(total)