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


def write_with_xslt(tree, filename, xslt_path):
    with open(filename, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(b'<?xml-stylesheet type="text/xsl" href="' + xslt_path.encode('utf-8') + b'"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False)


def main():
    print("Generating XML file...")
    bib_entries = get_bib_entries()
    # Create the root element
    bibliography = et.Element("bibliography")
    title = et.SubElement(bibliography, "bibtitle")
    title.text = "DBS Projekt BIB orginal"
    author = et.SubElement(bibliography, "author")
    author.text = "Nived Stephen, Lukas Ruminski"
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
    write_with_xslt(tree, "../files/bibEntries.xml", "../files/bibEntries.xsl")
    unescape_html_entities("../files/bibEntries.xml")
    parse_xml()
    tqdm.write("XML file generated successfully at ../files/bibEntries.xml.")


if __name__ == "__main__":
    main()
