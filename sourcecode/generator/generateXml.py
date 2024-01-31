import xml.etree.ElementTree as et
from sourcecode.generator.bibtexParseEntries import get_all_entries
from sourcecode.model.bibEntry import BibEntry
from sourcecode.model.bibEntryTypes import BibEntryTypes


# write a function that returns the BibEntryTypes based on the entry type
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


def main():
    bib_entries_from_file = get_all_entries()
    bib_entries = []
    for bib_entry in bib_entries_from_file:
        bib_entries.append(pass_bib_entry_to_model(bib_entry))
    # Create the root element
    bibliography = et.Element("bibliography")
    title = et.SubElement(bibliography, "title")
    title.text = "DBS_Projekt_BIB_orginal"
    author = et.SubElement(bibliography, "author")
    author.text = "Nived Stephen, Lukas Ruminski"
    BibEntry = et.SubElement(bibliography, "bibentries")

    # Iterate over the bib_entries and create XML elements for each one
    for bib_entry in bib_entries:
        bib_entry_element = et.SubElement(BibEntry, "bibentry", attrib={"id": bib_entry.id, "type": bib_entry.type})
        for field in bib_entry.required_fields.union(bib_entry.optional_fields):
            if hasattr(bib_entry, field):
                et.SubElement(bib_entry_element, field).text = str(getattr(bib_entry, field))

    # Create the XML document
    tree = et.ElementTree(bibliography)

    # Write the XML document to a file
    tree.write("bibentries.xml")


if __name__ == "__main__":
    main()
