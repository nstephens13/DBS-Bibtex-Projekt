import html
import xml.etree.ElementTree as ET


def replace_symbols(text):
    text = html.unescape(text)
    return text


# Parse the XML file
tree = ET.parse('../files/bibEntries.xml')

# Get the root element
root = tree.getroot()

# Iterate over all elements in the tree
for element in root.iter():
    for(child) in element:
        child.text = replace_symbols(str(child.text))
        print(child.text)

# Write the modified XML back to the file
tree.write('../files/bibEntries.xml', encoding='utf-8', xml_declaration=True)