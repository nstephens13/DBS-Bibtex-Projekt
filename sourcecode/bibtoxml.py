import re
import bibtexparser
import xml.etree.ElementTree as ET
import html

def handle_formatting(text):
    """Helper function to handle BibTeX formatting commands"""
    if '\\bf' in text:
        return {'text': text.replace('\\bf', ''), 'style': 'bold'}
    else:
        return {'text': text}

def remove_curly_braces(text):
    """Helper function to remove curly braces from the text"""
    return text.strip('{}')

def remove_parentheses(text):
    """Helper function to remove parentheses from the text"""
    return text.strip('()')

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

def handle_special_characters(text):
    """Helper function to handle special characters and formatting"""
    # Use regular expressions to find and replace special characters
    special_characters = {
        r'\\([^\s\\]+)': lambda match: html.unescape(match.group(0)),
        r'{\\o}': 'ø',
        r'{\\O}': 'Ø',
        r'{\\ae}': 'æ',
        r'{\\AE}': 'Æ',
        r'{\\aa}': 'å',
        r'{\\AA}': 'Å',
        r'{\\ss}': 'ß',
        r'\\"{a}': 'ä',
        r'\\"{A}': 'Ä',
        r'\\"{o}': 'ö',
        r'\\"{O}': 'Ö',
        r'\\"{u}': 'ü',
        r'\\"{U}': 'Ü',
    }

    for pattern, replace_function in special_characters.items():
        text = re.sub(pattern, replace_function, text)

    return text


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
                if field == 'volume':
                    formatted_text = handle_formatting(value)
                    field_element.text = formatted_text['text']
                    if 'style' in formatted_text:
                        field_element.set('style', formatted_text['style'])
                elif field in ['title', 'booktitle']:
                    field_element.text = remove_curly_braces(handle_special_characters(value))
                elif field == 'editor':
                    field_element.text = handle_special_characters(value)
                elif field == 'year':
                    field_element.text = remove_parentheses(value)
                else:
                    field_element.text = handle_special_characters(value)

    tree = ET.ElementTree(root)
    indent(root)
    
    try:
        tree.write(output_file_path, encoding="utf-8", xml_declaration=True)
        print(f"XML file '{output_file_path}' generated successfully.")
    except Exception as e:
        print(f"Error writing XML file: {e}")

if __name__ == "__main__":
    bibtex_file_path = '../data/Projekt_BIB_original.txt'
    output_file_path = 'output.xml'
    bibtex_to_xml(bibtex_file_path, output_file_path)
