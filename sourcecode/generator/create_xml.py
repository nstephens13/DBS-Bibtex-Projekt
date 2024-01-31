import xml.etree.ElementTree as et


class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


# Create some books
books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 180, 10.99),
    Book("To Kill a Mockingbird", "Harper Lee", 281, 7.99),
]

# Create the root element
root = et.Element("library")

# Iterate over the books and create XML elements for each one
for book in books:
    book_element = et.SubElement(root, "book", attrib={"title": book.title, "author": book.author})
    et.SubElement(book_element, "pages").text = str(book.pages)
    et.SubElement(book_element, "price").text = str(book.price)

# Create the XML document
tree = et.ElementTree(root)

# Write the XML document to a file
tree.write("library.xml")
