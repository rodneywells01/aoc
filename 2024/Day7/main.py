f = open("input.txt")

class Node():
    def __init__(self, operation, current_value, target, values):
        self.current_value = current_value
        self.target = target
        self.values = values
        self.operation = operation

    def evaluate(self):

        """
        If too much, return 1
        If too little, return -1
        If correct, return 0
        """

        if len(self.values) == 0:
            if self.current_value == self.target:
                print(f"{self.current_value} found valid")
                return 0
            elif self.current_value > self.target:
                return 1
            else:
                return -1


        if self.operation == "+":
            self.current_value += self.values[0]


        if self.operation == "*":
            self.current_value *= self.values[0]

        if self.operation == "||":
            self.current_value = int(str(self.current_value) + str(self.values[0]))

        self.values = self.values[1:]

        if self.current_value <=  self.target:
            evaluation_result = Node(
                operation="*",
                current_value=self.current_value,
                target=self.target,
                values = self.values
            ).evaluate()

            if evaluation_result == 0:
                return evaluation_result

            evaluation_result = Node(
                operation="+",
                current_value=self.current_value,
                target=self.target,
                values = self.values
            ).evaluate()

            if evaluation_result == 0:
                return evaluation_result

            evaluation_result = Node(
                operation="||",
                current_value=self.current_value,
                target=self.target,
                values = self.values
            ).evaluate()


            return evaluation_result
        else:
            return 1



class Tree():
    def __init__(self, target, values):
        res = Node(
            operation="*",
            current_value=values[0],
            target=target,
            values = values[1:]
        ).evaluate()

        if res == 0:
            self.valid = True
            print(f"{target} Valid")


        else:
            res = Node(
                operation="+",
                current_value=values[0],
                target=target,
                values = values[1:]
            ).evaluate()

            if res == 0:
                self.valid = True
                print(f"{target} Valid")

            else:
                res = Node(
                    operation="||",
                    current_value=values[0],
                    target=target,
                    values = values[1:]
                ).evaluate()
                if res == 0:
                    self.valid = True
                    print(f"{target} Valid")
                else:
                    self.valid = False
                    print(f"{target} NOT valid")


"""
Primary idea:
- Build a tree and solve the problem in real time.
"""

valid_stuff = list()
valid_total = 0

for line in f:
    target, values = [piece.strip() for piece in line.split(":")]
    target = int(target)
    values = [int(value) for value in values.split()]


    # Try math operations
    tree= Tree(target, values)
    if tree.valid:
        valid_stuff.append(line)
        valid_total += target



print("FINAL RESULTS")
for line in valid_stuff:
    print(line)

print(valid_total)


