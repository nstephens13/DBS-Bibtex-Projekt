import bibtexparser
import xml.etree.ElementTree as ET

def indent(elem, level=0):
    """Helper function to add indentation to XML elements"""
    i = "\n" + level * "    "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "    "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def bibtex_to_xml(bibtex_file_path, output_file_path):
    with open(bibtex_file_path, 'r', encoding='utf-8') as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    
    root = ET.Element("references")

    for entry in bib_database.entries:
        entry_type = entry['ENTRYTYPE'].lower()
        entry_element = ET.SubElement(root, entry_type)

        for field, value in entry.items():
            if field != 'ENTRYTYPE':
                field_element = ET.SubElement(entry_element, field.lower())
                field_element.text = value

    tree = ET.ElementTree(root)
    indent(root)
    tree.write(output_file_path, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    bibtex_file_path = '../data/Projekt_BIB_original.txt'
    output_file_path = 'output.xml'
    bibtex_to_xml(bibtex_file_path, output_file_path)
