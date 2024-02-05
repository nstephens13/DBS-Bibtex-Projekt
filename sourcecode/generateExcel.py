import os
import pandas as pd
from sourcecode.generator.bibtexParseEntries import get_bib_entries
from sourcecode.stringParser import clean_text
from tqdm import tqdm


def generate_excel():
    print("Generating Excel file...")
    bib_entries = get_bib_entries()
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
    directory = "../files"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the DataFrame to an Excel file
    df.to_excel("../files/bibEntries.xlsx", index=False)
    print("Excel file 'bibEntries.xlsx' generated successfully.")


if __name__ == "__main__":
    generate_excel()
