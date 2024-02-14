from tqdm import tqdm
import os

def generate_leet_combinations(word, leet_map, max_combinations_per_word):
    # Helper function to recursively generate combinations
    def generate_combinations(word, index, current_combination):
        if index == len(word):
            combinations.append(current_combination)
            return
        char = word[index]
        if char.lower() in leet_map:
            for leet_char in leet_map[char.lower()]:
                generate_combinations(word, index + 1, current_combination + leet_char)
                if len(combinations) >= max_combinations_per_word:
                    return
        else:
            generate_combinations(word, index + 1, current_combination + char)

    # Initialize list to store combinations
    combinations = []
    # Generate combinations recursively
    generate_combinations(word, 0, "")
    return combinations

def get_max_mutations():
    while True:
        max_mutations_input = input("Max mutations per word (default: 1000): ")
        if max_mutations_input.lower() == 'exit':
            print("Exiting script.")
            return None
        elif max_mutations_input.strip() == '':
            return 1000
        try:
            max_mutations = int(max_mutations_input)
            return max_mutations
        except ValueError:
            print("Invalid number. Type a number or 'exit' to quit.")

def get_min_length():
    while True:
        min_length_input = input("Skip words of length < # (default: 1): ")
        if min_length_input.lower() == 'exit':
            print("Exiting script.")
            return None
        elif min_length_input.strip() == '':
            return 1
        try:
            min_length = int(min_length_input)
            return min_length
        except ValueError:
            print("Invalid length. Type a number or 'exit' to quit.")

def get_max_chunk_size():
    while True:
        max_chunk_size_input = input("Max chunk size in KB (default: 1024): ")
        if max_chunk_size_input.lower() == 'exit':
            print("Exiting script.")
            return None
        elif max_chunk_size_input.strip() == '':
            return 1024
        try:
            max_chunk_size = int(max_chunk_size_input)
            return max_chunk_size
        except ValueError:
            print("Invalid size. Type a number or 'exit' to quit.")

def process_file_with_no_duplicates(leet_map, max_chunk_size=1024):
    input_file_name = input("Enter the input file name (with extension): ")

    output_file_name = input_file_name.rsplit('.', 1)[0] + "_leet_nd.txt"

    min_length = get_min_length()
    if min_length is None:
        return  # Exit the script if the user chooses to exit

    max_mutations = get_max_mutations()
    if max_mutations is None:
        return  # Exit the script if the user chooses to exit

    max_chunk_size = get_max_chunk_size()
    if max_chunk_size is None:
        return  # Exit the script if the user chooses to exit

    skipped_short_words_count = 0

    # Count the number of lines in the input file
    with open(input_file_name, 'r') as input_file:
        num_lines = sum(1 for _ in input_file)

    # Calculate the maximum number of lines per chunk to reach max_chunk_size
    with open(input_file_name, 'r') as input_file:
        line_size = sum(len(line) for line in input_file) / num_lines
    max_lines_per_chunk = int(max_chunk_size / line_size)

    num_chunks = num_lines // max_lines_per_chunk + (num_lines % max_lines_per_chunk != 0)

    with tqdm(total=num_chunks, desc="Processing", dynamic_ncols=True) as pbar:
        with open(input_file_name, 'r') as input_file:
            while True:
                chunk = []
                current_size = 0
                while current_size < max_chunk_size:
                    line = input_file.readline()
                    if not line:
                        break
                    chunk.append(line)
                    current_size += len(line.encode())
                
                if not chunk:
                    break
                
                combinations_chunk = []
                for line in chunk:
                    word = line.strip()
                    if len(word) < min_length:
                        skipped_short_words_count += 1
                        continue
                    combinations_chunk.extend(generate_leet_combinations(word, leet_map, max_mutations))
                
                with open(output_file_name, 'a') as output_file:
                    for combo in combinations_chunk:
                        output_file.write(combo + '\n')

                del combinations_chunk[:]  # Clear combinations_chunk list to free memory

                pbar.update(1)
        
        # Set progress bar to 100% after processing all chunks
        pbar.n = pbar.total
        pbar.refresh()

    print(f"Total words skipped due to length < {min_length}: {skipped_short_words_count}")

# Full leet_map with case-insensitive handling unchanged
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
