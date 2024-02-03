import xml.etree.ElementTree as et
from sourcecode.generator.bibtexParseEntries import get_bib_entries


def main():
    bib_entries = get_bib_entries()
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
    tree.write("../files/bibEntries.xml", encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
