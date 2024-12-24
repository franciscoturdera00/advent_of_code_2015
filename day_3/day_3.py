
text_file = "day_3/input.txt"
# text_file = "day_3/example.txt"
# text_file = "day_3/simple_example.txt"

def main():
    directions = read_input(text_file)
    santa_moves = [dir for i, dir in enumerate(directions) if i % 2 == 0]
    robo_moves = [dir for i, dir in enumerate(directions) if i % 2 == 1]
    houses, visited = count_lucky_houses((0, 0), santa_moves)
    robo_houses, _ = count_lucky_houses((0, 0), robo_moves, visited)
    return houses + robo_houses - 1
    # return houses

def read_input(file):
    with open(file) as f:
        return f.readline()

def count_lucky_houses(start, directions, visited=set()):
    unique_houses = 1
    location = start
    visited.add(start)
    for dir in directions:
        location = tuple(map(sum, zip(location, cardinal_direction(dir))))
        if location in visited:
            continue
        unique_houses += 1
        visited.add(location)
    return unique_houses, visited

def cardinal_direction(direction):
    match direction:
        case "^":
            return (0, -1)
        case ">":
            return (1, 0)
        case "v":
            return (0, 1)
        case "<":
            return (-1, 0)
        
print(main())