from sourcecode.model.bibtexReference import BibtexReference
from sourcecode.model.bibtexReferenceTypes import BibtexReferenceTypes

# Example usage
bibtex_reference = BibtexReference("Abadie/Eilers/Exel:98", BibtexReferenceTypes.article)
bibtex_reference.add_field("author", "John Doe")
bibtex_reference.add_field("title", "A Title")
bibtex_reference.add_field("journal", "Journal of Something")
bibtex_reference.add_field("year", "2022")
bibtex_reference.add_field("volume", "3")
bibtex_reference.add_field("pages", "1-10")

# Generate BibTeX
bibtex_entry = bibtex_reference.generate_bibtex()
print(bibtex_entry)
