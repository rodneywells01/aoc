from collections import defaultdict
from threading import local
f = open("input.txt")
rules = list()
updates = list()

next_format = False
for line in f:
    line = line.rstrip()
    if line == "":
        next_format = True
    elif not next_format:
        rules.append(line)
    else:
        updates.append(line)


performed_updates = set()
required_updates = defaultdict(list)


for rule in rules:
    requirements = rule.split("|")
    required_updated_value = requirements[0]
    value = requirements[1]
    required_updates[value].append(required_updated_value)

print(rules)
print(updates)
print(required_updates)

valid_middle_numbers = list()
incorrectly_ordered_lines = list()
for updateline in updates:
    performed_updates = set()
    valid = True
    update_set = set(updateline.split(","))
    # print(f"Testing {updateline}")
    for update in updateline.split(","):
        # print("Here")
        require_update_set = set(required_updates[update])
        # print(set(required_updates[update]))
        missing_updates = require_update_set.intersection(update_set) - performed_updates
        # print(missing_updates)
        if len(missing_updates) != 0:
            # print("Missed an update")
            valid = False
            break
        performed_updates.add(update)



    if valid:
        # print("Valid")
        # print(updateline)
        update_value_list=updateline.split(",")
        valid_middle_numbers.append(int(update_value_list[int((len(update_value_list) -1) / 2)]))
    else:
        incorrectly_ordered_lines.append(updateline)



print(valid_middle_numbers)
print(sum(valid_middle_numbers))

## Part 2

print(incorrectly_ordered_lines)


def part_two(incorrectly_ordered_lines):
    valid_middle_numbers = list()
    for updateline in incorrectly_ordered_lines:
        performed_updates = set()
        valid = False
        update_set = set(updateline.split(","))
        # print(f"Testing {updateline}")

        local_update_line = updateline
        # print(local_update_line)
        # raise Exception("done")

        while not valid:
            rectified = True
            for update in local_update_line.split(","):
                require_update_set = set(required_updates[update])
                missing_updates = require_update_set.intersection(update_set) - performed_updates
                # print(missing_updates)
                if len(missing_updates) != 0:
                    rectified = False
                    for missing_update in list(missing_updates):
                        # Need to reorder. Strategy:
                        # - Place required updates before this.
                        # - Restart from the beginning.
                        int_local_upldate_line = [int(val) for val in local_update_line.split(",")]
                        print(int_local_upldate_line)

                        # Remove the missing update
                        idx = int_local_upldate_line.index(int(missing_update))
                        front = int_local_upldate_line[:idx]
                        back = int_local_upldate_line[idx + 1:]
                        int_local_upldate_line = front + back
                        # print("Phase 1:")
                        # print(int_local_upldate_line)
                        # Insert it before the value that needs this update
                        idx = int_local_upldate_line.index(int(update))
                        front = int_local_upldate_line[:idx]
                        back = int_local_upldate_line[idx:]
                        # print("Phase 2")
                        # print(idx)
                        # print(front)
                        # print(back)
                        int_local_upldate_line = front + [int(missing_update)] + back

                        # print("Results")
                        # print(int_local_upldate_line)

                        local_update_line = ",".join([str(val) for val in int_local_upldate_line])
                        # print(local_update_line)



                    # Restart
                    break
                performed_updates.add(update)

            valid = rectified

        print("Valid")
        print(local_update_line)
        update_value_list=local_update_line.split(",")
        valid_middle_numbers.append(int(update_value_list[int((len(update_value_list) -1) / 2)]))

    print(valid_middle_numbers)
    print(sum(valid_middle_numbers))

part_two(incorrectly_ordered_lines)