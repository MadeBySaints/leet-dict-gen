# leet-dict-gen
convert any .txt dictionary into a larger leetspeak enabled dictionary

notes: included wpa.txt for testing. (caution: Generates a ~250MB file with all the combinations)

Leet Dict Gen requires python to run. simply place in the folder with the text file you want to convert, open a cmd prompt in that folder
enter into command prompt:
python leet.py
you will be asked to enter the file name you want to convert (path to file if not in same folder)

This can be used to generate massive dictionaries for pentesting/bruteforce testing.

Leet Dict Gen follows several rules:

1.User Input for Source File: It prompts the user to input the path of the source file from which they want to generate leet (1337) combinations. This path can be a simple file name if the file is in the same directory as the script or a full path to the file's location.

2.Automatic Output File Naming: Based on the input file name provided by the user, the script automatically generates an output file name by appending _leet_nd.txt to the base name of the input file. This naming convention helps in identifying the output file as containing leet combinations without duplicates, derived from the original source file.

3.Leet Combinations Generation: For each line in the source file, the script generates all possible leet combinations based on a predefined mapping (leet_map) that associates certain letters and numbers with their leet equivalents. This process involves recursive combination generation to cover all possible leet representations of a word.

4.Duplicate Removal: As it generates leet combinations, the script ensures that each combination is unique within the output file. It achieves this by maintaining a set of seen lines (seen_lines). Before writing a combination to the output file, it checks if the combination is already in the set. If not, the combination is written to the file and added to the set, ensuring no duplicates are produced.

5.Reporting Duplicates: When a duplicate combination is generated, rather than writing it to the output file, the script reports this by printing a message indicating that a duplicate was removed. This feedback can be useful for understanding how many and which duplicates were encountered and removed during processing.

6.Leet Map Customization: The leet_map dictionary defines the mappings from standard alphabetic characters and numbers to their leet equivalents. This map is crucial for generating the leet combinations and can be customized to include more or fewer equivalences based on the user's requirements.

The script combines text processing, user interaction, and file handling in Python to automate the generation of leet text from a source file while ensuring uniqueness and providing feedback on duplicate removal. This tool can be particularly useful for creating variant datasets, such as for password cracking exercises, testing databases for unique constraints, or any other application requiring unique combinations of leet text.
