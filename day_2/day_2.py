
import numpy


text_file = "day_2/input.txt"

def main():
    dimensions = read_input(text_file)
    return calculate_all_ribbon_needed(dimensions)

def read_input(file):
    dimensions = list()
    with open(file) as f:
        line = f.readline()
        while line:
            dimensions.append([int(d) for d in line.split("x")])
            line = f.readline()
        return dimensions
    
def calculate_paper_needed(dimension):
    side1 = dimension[0] * dimension[1]
    side2 = dimension[0] * dimension[2]
    side3 = dimension[1] * dimension[2]
    sides = [side1, side2, side3]
    smallest = min(sides)
    return sum([side * 2 for side in sides]) + smallest

def calculate_all_paper_needed(dimensions):
    return sum(calculate_paper_needed(dim) for dim in dimensions)

def calculate_ribbon_length_needed(dimension):
    perimeter = sum(sorted(dimension)[:2]) * 2
    volume = int(numpy.prod(dimension))
    return perimeter + volume

def calculate_all_ribbon_needed(dimensions):
    return sum(calculate_ribbon_length_needed(dim) for dim in dimensions)

    
print(main())