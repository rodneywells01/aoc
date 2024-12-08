from collections import defaultdict

def load_map():
    f = open("input.txt")
    map = list()
    for line in f:
        map.append(list(line.rstrip()))
    return map

class GuardSimulation():
    def __init__(self):
        self.map = load_map()
        self.available_loop_obstacle = True
        self.velocity = {
            "<": {
                "x": -1,
                "y": 0
            },
            ">": {
                "x": 1,
                "y": 0
            },
            "^": {
                "x": 0,
                "y": -1
            },
            "v": {
                "x": 0,
                "y": 1
            }
        }
        self.locations_visited = 0
        self.prior_positions = defaultdict(set)
        self.loop_inflicting_positions = set()

        # Find the guard
        guard_symbols = set(["<", ">", "^", "v"])
        found = False
        for row_idx in range(len(self.map)):
            for col_idx in range(len(self.map[row_idx])):
                if self.map[row_idx][col_idx] in guard_symbols:
                    self.guard_row_idx = row_idx
                    self.guard_col_idx = col_idx
                    self.guard = self.map[row_idx][col_idx]
                    found = True
                    break

            if found:
                break

        if not found:
            raise Exception("Guard was not present in input!")


    def is_done(self):
        # Sim is done when guard is at edge and leaving.
        return self.guard_row_idx == 0 and self.guard == "^" or \
            self.guard_row_idx == len(self.map)-1 and self.guard == "v" or \
            self.guard_col_idx == 0 and self.guard == "<" or \
            self.guard_col_idx == len(self.map[self.guard_row_idx])-1 and self.guard == ">"

    def is_loop(self):
        # res = self.guard in self.prior_positions[f"{self.guard_row_idx},{self.guard_col_idx}"]
        return self.guard in self.prior_positions[f"{self.guard_row_idx},{self.guard_col_idx}"]

    def rotate_guard(self):
        # Guard always rotates right
        next_position = {
            "<": "^",
            "^": ">",
            ">": "v",
            "v": "<"
        }

        self.guard = next_position[self.guard]
        self.map[self.guard_row_idx][self.guard_col_idx] = self.guard


    def display_map(self):
        # Print a smaller map

        print()
        print(f"==========")
        for row in self.map:
            print(row)
        print("==========")
        print()

        input()

    def display_map_tiny(self):
        # Print a smaller map

        print()
        delta = 10
        print(f"=========={self.guard_row_idx-delta}")
        rows = self.map[self.guard_row_idx-delta:self.guard_row_idx+delta]
        for row in rows:
            print(row[self.guard_col_idx-delta:self.guard_col_idx+delta])
        print(f"=========={self.guard_row_idx+delta}")
        print()

        input()


    def move_guard(self, find_loop=False):
        next_row_idx = self.guard_row_idx + self.velocity[self.guard]["y"]
        next_col_idx = self.guard_col_idx + self.velocity[self.guard]["x"]
        next_position = self.map[next_row_idx][next_col_idx]

        if next_position == "#":
            # Obstacle hit.
            self.rotate_guard()
        else:
            if find_loop and self.available_loop_obstacle and \
                f"{next_row_idx},{next_col_idx}" not in self.loop_inflicting_positions:

                # Attempt to place obstacle to find loop
                loop_test_sim = GuardSimulation()
                loop_test_sim.available_loop_obstacle = False
                loop_test_sim.map[next_row_idx][next_col_idx] = "#"
                is_loop = loop_test_sim.run_simulation_find_loop()

                if is_loop:
                    self.loop_inflicting_positions.add(f"{next_row_idx},{next_col_idx}")
                    print(len(self.loop_inflicting_positions))

            # Mark current position as visited
            self.map[self.guard_row_idx][self.guard_col_idx] = "X"

            # Move forward
            self.map[next_row_idx][next_col_idx] = self.guard
            self.guard_row_idx = next_row_idx
            self.guard_col_idx = next_col_idx

    def calculate_unique_locations_visited(self):
        total = 1 # Guard counts as a location visited
        for row in self.map:
            for col in row:
                if col == "X":
                    total += 1
        return total


    def run_simulation(self):
        steps = 0
        while not self.is_done():
            self.move_guard()
            steps += 1
            print(steps)

        self.display_map()
        print(steps)
        print(f"Visited {self.calculate_unique_locations_visited()} locations")
        print("Done!")

    def run_simulation_find_loop(self):
        is_loop = False
        self.prior_positions[f"{self.guard_row_idx},{self.guard_col_idx}"].add(self.guard)
        while not self.is_done():
            self.move_guard(find_loop=True)
            if not self.available_loop_obstacle and self.is_loop():
                # self.display_map_tiny()
                is_loop = True
                break
            self.prior_positions[f"{self.guard_row_idx},{self.guard_col_idx}"].add(self.guard)


        if self.available_loop_obstacle:
            print("Found these loop inflicting placements:")
            print(self.loop_inflicting_positions)
            print(len(self.loop_inflicting_positions))

        return is_loop

sim = GuardSimulation()
# sim.run_simulation()
sim.run_simulation_find_loop()
