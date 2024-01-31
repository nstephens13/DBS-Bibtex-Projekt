from sourcecode.model.bibEntry import BibEntry
from sourcecode.model.bibEntryTypes import BibEntryTypes

# Example usage
bib_entry = BibEntry("Abadie/Eilers/Exel:98", BibEntryTypes.article)
bib_entry.add_field("author", "John Doe")
bib_entry.add_field("title", "A Title")
bib_entry.add_field("journal", "Journal of Something")
bib_entry.add_field("year", "2022")
bib_entry.add_field("volume", "3")
bib_entry.add_field("pages", "1-10")

# Generate BibTeX
bibtex_entry = bib_entry.generate_bibtex()
print(bibtex_entry)
