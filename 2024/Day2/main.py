def part_one():

    def validate_inc_dec_rule(report):
        """
        The levels are either all increasing or all decreasing.
        """
        x = 0
        return all(report[x] < report[x + 1] for x in range(len(report) - 1 )) \
            or all(report[x] > report[x + 1] for x in range(len(report) - 1 ))


    def validate_adjacency_rule(report):
        """
        Any two adjacent levels differ by at least one and at most three.
        """
        l_diff = 0

        for x in range(1, len(report)):
            l_diff = abs(report[x] - report[x-1])
            if not(1 <= l_diff <= 3):
                return False

        return True

    safe_count = 0
    safe_res = list()
    for line in f:
        report = [int(x) for x in line.split()]
        print(report)
        # res = validate_inc_dec_rule(report)
        # print(res)

        # res = validate_adjacency_rule(report)
        # print(res)
        is_safe = validate_adjacency_rule(report) and validate_inc_dec_rule(report)
        safe_res.append(is_safe)
        if is_safe:
            safe_count += 1

    print(f"safe_count: {safe_count}")
    return safe_res

def part_two():
    def validate_inc(report, dampener=True):
        for x in range(len(report) - 1):
            if report[x] < report[x + 1]:
                continue
            elif dampener:
                # Can we salvage this with a dampener?
                print("Spending a dampener")

                # Need to check if removing x can help, or removing x+1 can help
                left = x
                right = x + 1

                # Omit x
                new_report = report[:left] + report[right:]
                valid = validate_inc(new_report, dampener=False)
                if valid and validate_adjacency_rule(new_report, dampener=False):
                    print("Removing x works")
                    return True

                # Omit x + 1
                new_report = report[:left + 1] + report[right + 1:]
                valid = validate_inc(new_report, dampener=False)
                if valid and validate_adjacency_rule(new_report, dampener=False):
                    print("Removing x+1 works")
                    return True

                return False
            else:
                return False

        return validate_adjacency_rule(report, dampener)

    def validate_dec(report, dampener=True):
        for x in range(len(report) - 1):
            if report[x] > report[x + 1]:
                continue
            elif dampener:
                # Can we salvage this with a dampener?
                print("Spending a dampener")

                # Need to check if removing x can help, or removing x+1 can help
                left = x
                right = x + 1

                # Omit x
                new_report = report[:left] + report[right:]
                valid = validate_dec(new_report, dampener=False)
                if valid and validate_adjacency_rule(new_report, dampener=False):
                    print("Removing x works")
                    return True

                # Omit x + 1
                new_report = report[:left + 1] + report[right + 1:]
                valid = validate_dec(new_report, dampener=False)
                if valid and validate_adjacency_rule(new_report, dampener=False):
                    print("Removing x+1 works")
                    return True

                return False

            else:
                return False

        return validate_adjacency_rule(report, dampener)

    def validate_inc_dec_rule(report, dampener = True):
        """
        Check inc and ec first. if Valid, check for adjacency.
        """
        return validate_inc(report, dampener) or validate_dec(report, dampener)


    def validate_adjacency_rule(report, dampener=True):
        """
        Any two adjacent levels differ by at least one and at most three.
        """
        for x in range(len(report)-1):
            diff = abs(report[x] - report[x+1])
            if not(1 <= diff <= 3):
                if dampener:
                    left = x
                    right = x + 1

                    # Omit x
                    new_report = report[:left] + report[right:]
                    if validate_adjacency_rule(new_report, dampener=False):
                        return True

                    # Omit x + 1
                    new_report = report[:left + 1] + report[right + 1:]
                    if validate_adjacency_rule(new_report, dampener=False):
                        return True

                    return False
                else:
                    return False

        return True

    safe_count = 0
    safe_res = list()
    for line in f:
        report = [int(x) for x in line.split()]
        print(report)

        is_safe = validate_inc_dec_rule(report, dampener=True)
        print(is_safe)
        safe_res.append(is_safe)
        if is_safe:
            safe_count += 1
    print(f"safe_count: {safe_count}")
    print(safe_res)

    return safe_res

# f = open("input.txt")
# safe_res = part_one()
f = open("input.txt")
print("Starting part 2")
safe_res_damp = part_two()

