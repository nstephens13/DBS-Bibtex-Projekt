import bibtexparser
from sourcecode.model.bibEntry import BibEntry
from sourcecode.model.bibEntryTypes import BibEntryTypes


def get_all_entries(bibtex_file_path):
    with open(bibtex_file_path, 'r') as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database.entries


def get_entries_length():
    return len(get_all_entries())


def get_bib_entry_type(entry_type):
    if entry_type in BibEntryTypes.__members__:
        return BibEntryTypes[entry_type]
    else:
        raise ValueError(f"Entry type '{entry_type}' is not a valid BibEntryType.")


def pass_bib_entry_to_model(new_bib_entry):
    bib_entry = BibEntry(new_bib_entry["ID"], get_bib_entry_type(new_bib_entry["ENTRYTYPE"]))
    for field in new_bib_entry:
        if field != "ID" and field != "ENTRYTYPE":
            # Convert the field to lowercase
            field = field.lower()
            bib_entry.add_field(field, new_bib_entry[field])
    return bib_entry


def get_bib_entries(bibtex_file_path):
    bib_entries_from_file = get_all_entries(bibtex_file_path)
    bib_entries = []
    for bib_entry in bib_entries_from_file:
        bib_entries.append(pass_bib_entry_to_model(bib_entry))
    return bib_entries
