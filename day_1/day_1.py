
# text_file = "day_1/example.txt"   
text_file = "day_1/input.txt"

def main():
    parens = read_input(text_file)
    return find_first_basement_index(parens)

def read_input(file):
    with open(file) as f:
        return f.readline()
    
def calculate_floor(parens):
    floor = 0
    for p in parens:
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1
    return floor

def find_first_basement_index(parens):
    floor = 0
    index = 1
    for p in parens:
        if p == "(":
            floor += 1
        elif p == ")":
            floor -= 1
        if floor == -1:
            return index
        index += 1
    return -1
    
print(main())