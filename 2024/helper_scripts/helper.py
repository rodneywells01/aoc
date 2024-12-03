import os
import sys

print(sys.argv)


def generate_new_day(day_num):
    res = os.listdir()
    dir_name = f"Day{day_num}"

    try:
        os.makedirs(dir_name)
        f = open(f"{dir_name}/input.txt", "a")
        f.write("Hello, world!")
        f.close()

        f = open(f"{dir_name}/main.py", "a")
        f.write("Hello, world!")
        f.close()
    except FileExistsError:
        print(f"You've already made {dir_name}!")


for x in range(1, 26):
    generate_new_day(x)
