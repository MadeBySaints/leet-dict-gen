def generate_leet_combinations(word, leet_map):
    def generate_combos(chars):
        if not chars:
            return [""]
        combos = []
        first, rest = chars[0], chars[1:]
        for char in leet_map.get(first.lower(), [first]):
            for combo in generate_combos(rest):
                combos.append(char + combo)
        return combos

    combinations = generate_combos(word)
    
    unique_combinations = set()
    for combo in combinations:
        if combo not in unique_combinations and not any(combo[i:i+4] == combo[i]*4 for i in range(len(combo)-3)):
            unique_combinations.add(combo)

    return list(unique_combinations)

def process_file_with_no_duplicates(leet_map):
    input_file_path = input("Enter the path to your source file: ")
    # Automatically generate the output file path by appending '_leet_nd.txt' to the input file name (before the file extension if present)
    if '.' in input_file_path:
        output_file_path = input_file_path.rsplit('.', 1)[0] + '_leet_nd.txt'
    else:
        output_file_path = input_file_path + '_leet_nd.txt'

    seen_lines = set()
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
        for line in input_file:
            word = line.strip()
            combinations = generate_leet_combinations(word, leet_map)
            for combo in combinations:
                if combo not in seen_lines:
                    output_file.write(combo + '\n')
                    seen_lines.add(combo)
                else:
                    print(f"Duplicate removed: {combo}")

# Leet map definition
leet_map = {
    'a': ['a', '4'], 'b': ['b', '8'], 'c': ['c'], 'd': ['d'], 'e': ['e', '3'],
    'f': ['f'], 'g': ['g', '9'], 'h': ['h'], 'i': ['i', '1'], 'j': ['j'],
    'k': ['k'], 'l': ['l', '1'], 'm': ['m'], 'n': ['n'], 'o': ['o', '0'],
    'p': ['p'], 'q': ['q'], 'r': ['r'], 's': ['s', '5'], 't': ['t', '7'],
    'u': ['u'], 'v': ['v'], 'w': ['w'], 'x': ['x'], 'y': ['y'], 'z': ['z'],
    '0': ['0', 'o'], '1': ['1', 'l', 'i'], '2': ['2'], '3': ['3', 'e'], 
    '4': ['4', 'a'], '5': ['5', 's'], '6': ['6'], '7': ['7', 't'], '8': ['8', 'b'], '9': ['9', 'g']
}

# Example usage now with user input for file names and integrated functionality
process_file_with_no_duplicates(leet_map)
