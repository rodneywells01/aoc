from collections import defaultdict

f = open("input.txt")

left = list()
right = list()

def part_one():
    for line in f:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))


    def generate_differences(left, right):
        differences = list()
        x = 0
        while x < len(left):
            differences.append(abs(left[x] - right[x]))
            x += 1

        return differences

    left.sort()
    right.sort()

    differences = generate_differences(left, right)

    print (f"Total distance: {sum(differences)}")

def part_two():

    def generate_frequency_dict(right):
        num_frequency = defaultdict(int)
        for x in right:
            num_frequency[x] += 1
        return num_frequency



    def calculate_similarity_score(left, frequency):
        similarity_score = 0
        for x in left:
            similarity_score += frequency[x] * x
        return similarity_score


    frequency = generate_frequency_dict(right)
    similarity_score = calculate_similarity_score(left, frequency)

    print(f"Similarity Score: {similarity_score}")



part_one()
part_two()