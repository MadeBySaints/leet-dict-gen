def generate_leet_combinations(word, leet_map):
    def generate_combos(chars):
        if not chars:
            return [""]
        combos = []
        first, rest = chars[0], chars[1:]
        # Retrieve substitutions, ensuring uniqueness with set
        substitutions = set(leet_map.get(first, [first]) + leet_map.get(first.lower(), []))
        for char in substitutions:
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

# Updated leet_map including all letters with uppercase, lowercase, and numeric leet equivalents
leet_map = {
    'a': ['a', 'A', '4'], 'A': ['A', 'a', '4'],
    'b': ['b', 'B', '8'], 'B': ['B', 'b', '8'],
    'c': ['c', 'C'], 'C': ['C', 'c'],
    'd': ['d', 'D'], 'D': ['D', 'd'],
    'e': ['e', 'E', '3'], 'E': ['E', 'e', '3'],
    'f': ['f', 'F'], 'F': ['F', 'f'],
    'g': ['g', 'G', '9'], 'G': ['G', 'g', '9'],
    'h': ['h', 'H'], 'H': ['H', 'h'],
    'i': ['i', 'I', '1'], 'I': ['I', 'i', '1'],
    'j': ['j', 'J'], 'J': ['J', 'j'],
    'k': ['k', 'K'], 'K': ['K', 'k'],
    'l': ['l', 'L', '1'], 'L': ['L', 'l', '1'],
    'm': ['m', 'M'], 'M': ['M', 'm'],
    'n': ['n', 'N'], 'N': ['N', 'n'],
    'o': ['o', 'O', '0'], 'O': ['O', 'o', '0'],
    'p': ['p', 'P'], 'P': ['P', 'p'],
    'q': ['q', 'Q'], 'Q': ['Q', 'q'],
    'r': ['r', 'R'], 'R': ['R', 'r'],
    's': ['s', 'S', '5'], 'S': ['S', 's', '5'],
    't': ['t', 'T', '7'], 'T': ['T', 't', '7'],
    'u': ['u', 'U'], 'U': ['U', 'u'],
    'v': ['v', 'V'], 'V': ['V', 'v'],
    'w': ['w', 'W'], 'W': ['W', 'w'],
    'x': ['x', 'X'], 'X': ['X', 'x'],
    'y': ['y', 'Y'], 'Y': ['Y', 'y'],
    'z': ['z', 'Z', '2'], 'Z': ['Z', 'z', '2']
}

# Execute the script
process_file_with_no_duplicates(leet_map)
