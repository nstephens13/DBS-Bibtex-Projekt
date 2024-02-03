import xml.etree.ElementTree as et
from sourcecode.generator.bibtexParseEntries import get_bib_entries
from sourcecode.stringParser import latex_to_mathml, clean_text


def main():
    print("Generating XML file...")
    bib_entries = get_bib_entries()
    # Create the root element
    bibliography = et.Element("bibliography")
    title = et.SubElement(bibliography, "title")
    title.text = "DBS_Projekt_BIB_orginal"
    author = et.SubElement(bibliography, "author")
    author.text = "Nived Stephen, Lukas Ruminski"
    bib_entries_element = et.SubElement(bibliography, "bibentries")

    # Iterate over the bib_entries and create XML elements for each one
    for bib_entry in bib_entries:
        bib_entry_element = et.SubElement(bib_entries_element, "bibentry", attrib={"id": bib_entry.id, "type": bib_entry.type})
        for field in bib_entry.required_fields.union(bib_entry.optional_fields):
            if hasattr(bib_entry, field):
                field_value = getattr(bib_entry, field)
                field_value = str(field_value)
                field_value = clean_text(field_value)
                field_value = latex_to_mathml(field_value)
                print(field_value)
                et.SubElement(bib_entry_element, field).text = field_value
                print(et.SubElement(bib_entry_element, field).text)

    # Create the XML document
    tree = et.ElementTree(bibliography)

    # Write the XML document to a file
    tree.write("../files/bibEntries.xml", encoding="utf-8", xml_declaration=True)
    print("XML file 'bibEntries.xml' generated successfully.")


if __name__ == "__main__":
    main()
