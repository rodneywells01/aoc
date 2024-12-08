import re

f = open("input.txt")

def execute_muls(mul_instructions, enabled):
    total = 0
    for inst in mul_instructions:
        print(f"Parsing: {inst}")
        if inst[0:3] == 'do(':
            enabled = True
            print("ENABLED")
        elif inst[0:5] == "don\'t":
            print("DISABLED")
            enabled = False
        elif enabled:
            mul_group = inst[4:len(inst)-1]
            mul_vals = mul_group.split(",")
            total += int(mul_vals[0]) * int(mul_vals[1])

    return total, enabled

total = 0
enabled = True
for instruction in f:
    matches = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|(don't\(\))|(do\(\)))", instruction)
    matches = [match[0] for match in matches]
    res, enabled = execute_muls(matches, enabled)
    total += res

print(total)
