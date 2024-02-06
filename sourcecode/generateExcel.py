import os
import pandas as pd
from sourcecode.generator.bibtexParseEntries import get_bib_entries
from sourcecode.stringParser import clean_text
from tqdm import tqdm


def get_file_path():
    print("Please enter the type of BIB file you want to generate Excel from:")
    print("1. Min")
    print("2. Max")
    print("3. Original")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        return "Projekt_BIB_min.txt"
    elif choice == "2":
        return "Projekt_BIB_max.txt"
    elif choice == "3":
        return "Projekt_BIB_original.txt"
    else:
        print("Invalid choice. Please try again.")
        return get_file_path()


def get_xml_file_path(file_path):
    return file_path.replace(".txt", ".xlsx")


def generate_excel():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to the 'Projekt_BIB_original.txt' file
    bibtex_file = get_file_path()
    bibtex_file_path = os.path.join(current_dir, 'data', bibtex_file)
    filepath = '../files/excel/' + get_xml_file_path(bibtex_file)
    print("Generating ", filepath, " from ", bibtex_file)
    print("Reading BIB file:", bibtex_file_path)
    bib_entries = get_bib_entries(bibtex_file_path)

    data = []
    # Iterate over the bib_entries and create a dictionary for each one
    for bib_entry in tqdm(bib_entries, desc="Processing entries", unit="entry"):
        entry_dict = {"id": bib_entry.id, "type": bib_entry.type}
        for field in bib_entry.required_fields.union(bib_entry.optional_fields):
            if hasattr(bib_entry, field):
                entry_dict[field] = str(getattr(bib_entry, field))
        data.append(entry_dict)

    # Create a DataFrame from the data
    df = pd.DataFrame(data)

    # Apply clean_text function to all columns
    df = df.apply(lambda col: col.map(clean_text) if col.dtype == 'O' else col)

    # Create the directory if it does not exist
    directory = "../files/excel/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the DataFrame to an Excel file
    df.to_excel(filepath, index=False)
    print("Excel file generated successfully at ", filepath)


if __name__ == "__main__":
    generate_excel()
