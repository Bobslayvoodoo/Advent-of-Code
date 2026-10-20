with open("Input.txt") as file:
    ranges = file.read().strip().split(",")

invalids = []
for r in ranges:
    start, finish = r.split("-")
    start, finish = int(start), int(finish)
    for number in range(start,finish+1):
        str_num = str(number)
        num_len = len(str_num)
        if num_len % 2 == 1:
            continue
        if str_num[:num_len//2] == str_num[num_len//2:]:
            invalids.append(number)
            
print(sum(invalids))
