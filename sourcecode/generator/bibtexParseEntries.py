import bibtexparser
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the 'Projekt_BIB_original.txt' file
bibtex_file_path = os.path.join(current_dir, '..', 'data', 'Projekt_BIB_original.txt')


def get_all_entries():
    with open(bibtex_file_path, 'r') as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database.entries


def get_entries_length():
    return len(get_all_entries())


# Print all entries
print(get_all_entries()[0])

# Print the number of entries
print(get_entries_length())
