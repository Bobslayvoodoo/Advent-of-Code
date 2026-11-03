ranges = []
ingredient_ids = []
with open("Input.txt") as file:
    for line in file:
        line = line.strip()
        if line == "":
            break
        
        line = line.split("-")
        new_range = [int(line[0]),int(line[1])]
        ranges.append(new_range)
        
# pointless optimisation? maybe. but it was fun
# makes part 2 easy haha
merged_ranges = []
for current_range in ranges:
    start_in_range = None
    end_in_range = None
    remove_range = None
    for merged_range_num, merged_range in enumerate(merged_ranges):
        # my start is in your range
        if merged_range[0] <= current_range[0] <= merged_range[1]:
            start_in_range = merged_range_num
            
        if merged_range[0] <= current_range[1] <= merged_range[1]:
            end_in_range = merged_range_num
            
        # i contain YOU
        if current_range[0] <= merged_range[0] and merged_range[1] <= current_range[1]:
            remove_range = merged_range_num
            
        if start_in_range != None and start_in_range == end_in_range:
            ## completely in another range: give up
            break
            
    if start_in_range != None and start_in_range == end_in_range:
            ## completely in another range: give up
            continue
        
    if start_in_range != None and end_in_range != None:
        ## merge two existing ranges
        lower_range = merged_ranges[start_in_range]
        higher_range = merged_ranges[end_in_range]
        lower_range[1] = higher_range[1]
        merged_ranges.pop(end_in_range)
        continue
    
    if start_in_range != None:
        ## extend existing range
        existing_range = merged_ranges[start_in_range]
        existing_range[1] = current_range[1]
        continue
    
    if end_in_range != None:
        ## extend but the opposite direction
        existing_range = merged_ranges[end_in_range]
        existing_range[0] = current_range[0]
        continue
    
    if remove_range != None:
        merged_ranges.pop(remove_range)
    # not in any range: add to pile
    merged_ranges.append(current_range)
    
    
fresh_count = 0
for current_range in merged_ranges:
    fresh_count += current_range[1] - current_range[0]
    fresh_count += 1 # inclusive


print(fresh_count)
            
            
            
            