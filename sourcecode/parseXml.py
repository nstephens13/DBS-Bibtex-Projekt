import re
import xml.etree.ElementTree as ET


def write_with_xslt(tree, filename, xslt_path):
    with open(filename, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(b'<?xml-stylesheet type="text/xsl" href="' + xslt_path.encode('utf-8') + b'"?>\n')
        tree.write(f, encoding='utf-8', xml_declaration=False)


def replace_ampersand(filename):
    with open(filename, 'r') as file:
        content = file.read()
    content = re.sub('&amp;#', '&#', content)
    content = re.sub('ä', '&#228;', content)
    content = re.sub(r'\\H &#305;', '&#305;&#779;', content)
    content = re.sub(r'\\u &#305', '&#301;', content)
    content = re.sub(r'\\c', '&#65533;c', content)
    with open(filename, 'w') as file:
        file.write(content)


def replace_non_ascii(s):
    # Find all HTML UTF-8 Unicode sequences
    html_unicode_sequences = re.findall(r'&#\d+;', s)

    # Initialize an empty list to store the modified characters
    modified_chars = []

    # Iterate over the characters in the string
    for char in s:
        # If the character is part of an HTML UTF-8 Unicode sequence, leave it as it is
        if any(char in seq for seq in html_unicode_sequences):
            modified_chars.append(char)
        # If the character is not part of an HTML UTF-8 Unicode sequence and its ASCII value is above 127,
        # replace it with its HTML UTF-8 Unicode
        elif ord(char) > 127:
            modified_chars.append(f'&#{ord(char)};')
        # If the character is not part of an HTML UTF-8 Unicode sequence and its ASCII value is 127 or below,
        # leave it as it is
        else:
            modified_chars.append(char)

    # Join the modified characters into a string and return it
    return ''.join(modified_chars)


def replace_non_ascii_with_html_entities(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Function to replace non-ASCII characters in text of an element
    def replace_chars(element):
        if element.text:
            element.text = replace_non_ascii(element.text)
        for child in element:
            replace_chars(child)

    # Replace characters in all elements
    replace_chars(root)

    # Write the modified XML back to the file using the custom writer
    write_with_xslt(tree, filename, "../files/Project_BIB.xsl")


def parse_xml(filename):
    replace_non_ascii_with_html_entities(filename)
    replace_ampersand(filename)
    print("Non-ASCII characters replaced successfully.")
