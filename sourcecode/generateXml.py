import os
import xml.etree.ElementTree as et
from sourcecode.generator.bibtexParseEntries import get_bib_entries
from sourcecode.parseXml import parse_xml
from sourcecode.stringParser import latex_to_mathml, clean_text
import html
import re
from tqdm import tqdm


def replace_ampersand(s):
    return re.sub(r'&(?![#])', '&amp;', s)


def unescape_html_entities(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    unescaped_content = html.unescape(content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(unescaped_content)


def write_with_xslt(tree, filename, bibtex_file, xslt_path):
    with open(filename, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(b'<?xml-stylesheet type="text/xsl" href="' + xslt_path.encode('utf-8') + b'"?>\n')
        f.write(b'<!DOCTYPE bibliography SYSTEM "Projekt_BIB.dtd">\n')
        tree.write(f, encoding='utf-8', xml_declaration=False)


def get_file_path():
    print("Please enter the type of BIB file you want to generate XML from:")
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
    return file_path.replace(".txt", ".xml")


def main():
    # Get the current directory of the script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the relative path to the 'Projekt_BIB_original.txt' file
    bibtex_file = get_file_path()
    bibtex_file_path = os.path.join(current_dir, 'data', bibtex_file)
    filepath = '../files/' + get_xml_file_path(bibtex_file)
    print("Generating ", filepath, " from ", bibtex_file)
    print("Reading BIB file:", bibtex_file_path)
    bib_entries = get_bib_entries(bibtex_file_path)

    # Create the root element
    bibliography = et.Element("bibliography")
    title = et.SubElement(bibliography, "bibtitle")
    title.text = 'DBS ' + bibtex_file.replace("_", " ").replace(".txt", "")
    author = et.SubElement(bibliography, "author")
    author.text = "Nived Stephen and Lukas Ruminski"
    bib_entries_element = et.SubElement(bibliography, "bibentries")

    # Iterate over the bib_entries and create XML elements for each one
    for bib_entry in tqdm(bib_entries, desc="Processing entries", unit="entry"):
        bib_entry_element = et.SubElement(bib_entries_element, "bibentry",
                                          attrib={"id": bib_entry.id, "type": bib_entry.type})
        for field in bib_entry.required_fields:
            if hasattr(bib_entry, field):
                field_value = getattr(bib_entry, field)
                field_value = str(field_value)
                field_value = clean_text(field_value)
                field_value = latex_to_mathml(field_value)
                field_value = replace_ampersand(field_value)
                et.SubElement(bib_entry_element, field).text = field_value
        for field in bib_entry.optional_fields:
            if hasattr(bib_entry, field):
                field_value = getattr(bib_entry, field)
                field_value = str(field_value)
                field_value = clean_text(field_value)
                field_value = latex_to_mathml(field_value)
                field_value = replace_ampersand(field_value)
                et.SubElement(bib_entry_element, field).text = field_value

    # Create the XML document
    tree = et.ElementTree(bibliography)
    write_with_xslt(tree, filepath, bibtex_file, "../files/Project_BIB.xsl")
    unescape_html_entities(filepath)
    parse_xml(filepath)
    print("XML file generated successfully at ", filepath)


if __name__ == "__main__":
    main()
