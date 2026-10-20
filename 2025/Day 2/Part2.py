with open("Input.txt") as file:
    ranges = file.read().strip().split(",")

invalids = []
for r in ranges:
    start, finish = r.split("-")
    start, finish = int(start), int(finish)
    for number in range(start,finish+1):
        str_num = str(number)
        num_len = len(str_num)
        if num_len % 2 == 0:
            if str_num[:num_len//2] == str_num[num_len//2:]:
                invalids.append(number)
                continue

        for repsize in range(1,(num_len//3)+1):
            if num_len % repsize != 0:
                continue
            pointer = 0
            while pointer + repsize < num_len:
                if str_num[pointer:pointer+repsize] != str_num[pointer+repsize:pointer+repsize*2]:
                    break
                pointer += repsize
            else:
                invalids.append(number)
                break
                  
print(sum(invalids))
