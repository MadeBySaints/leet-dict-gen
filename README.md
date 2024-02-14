# leet-dict-gen
Convert any .txt dictionary into a larger leetspeak enabled dictionary

This can be used to generate massive dictionaries for pentesting/bruteforce testing.

# Leet Combination Generator

## Overview
The Leet Combination Generator script takes a list of words from an input file and generates leet combinations for each word, applying common character substitutions according to the leet_map dictionary. It then writes the unique combinations to an output file, with each combination on a separate line.

## Specifications
- **Input**: Text file containing a list of words.
- **Output**: Text file containing unique leet combinations of the input words.
- **Character Substitutions**: The script applies common leet substitutions according to the provided leet_map dictionary.
- **Maximum Mutations per Word**: The user can specify the maximum number of mutations allowed per word.
- **Minimum Word Length**: The user can specify the minimum length of words to include in the generation process.
- **Maximum Chunk Size**: The user can specify the maximum size (in KB) of each chunk processed to control memory usage.

## Usage & Dependencies
1. Clone or download the repository to your local machine. Just the leet.py file will work.
2. Ensure you have Python installed on your system (version 3.6 or higher).
3. Install tqdm library using the following command:

pip install tqdm

5. Run the script using the following command:

python leet.py

6. Follow the prompts to provide the input file name, maximum mutations per word, minimum word length, and maximum chunk size.
7. The script will process the input file and generate leet combinations, showing progress with a live progress bar.
8. Once finished, the unique leet combinations will be written to the output file.

## Example
Suppose you have a file named `words.txt` containing the following words:
hello
world
leet
generator

You run the script and provide the input file name as `words.txt`, maximum mutations per word as `2`, minimum word length as `3`, and maximum chunk size as `1024 KB`. The script will then generate leet combinations for words with a minimum length of 3, applying a maximum of 2 mutations per word, and write the unique combinations to an output file named `words_leet_nd.txt`.

## Notes
- The script uses tqdm library to display a progress bar for the processing.
- Ensure you have appropriate permissions to read from the input file and write to the output file.
- ND simply stands for no duplicates
- Included wpa.txt for testing. (caution: Generates a ~250MB file with all the combinations)





