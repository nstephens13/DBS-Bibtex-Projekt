import re
from lxml import etree
from lxml.etree import CDATA


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
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(filename, parser)
    root = tree.getroot()

    # Function to replace non-ASCII characters in text of an element
    def replace_chars(element):
        if element.text:
            element.text = CDATA(replace_non_ascii(element.text))
        for child in element:
            replace_chars(child)

    # Replace characters in all elements
    replace_chars(root)

    # Write the modified XML back to the file
    tree.write(filename, encoding='utf-8', xml_declaration=True)


print("Replacing non-ASCII characters with HTML entities...")
replace_non_ascii_with_html_entities("../files/bibEntries.xml")
print("Non-ASCII characters replaced successfully.")