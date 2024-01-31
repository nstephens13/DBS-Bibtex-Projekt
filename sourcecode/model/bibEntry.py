from sourcecode.model.bibEntryTypes import BibEntryTypes


class BibEntry:
    def __init__(self, entry_id, entry_type):
        self.id = entry_id
        self.type = entry_type.name  # Get the name of the Enum member as a string
        self.required_fields = set()
        self.optional_fields = set()

        # Assign required and optional fields based on the reference type
        if self.type in BibEntryTypes.__members__:  # Check if the name is a valid Enum member
            self.required_fields.update(BibEntryTypes[self.type].value["required_fields"])
            self.optional_fields.update(BibEntryTypes[self.type].value["optional_fields"])

    def add_field(self, field, value):
        # Check if the field is allowed for this reference type
        if field in self.required_fields or field in self.optional_fields:
            setattr(self, field, value)
        else:
            raise ValueError(f"Field '{field}' is not allowed for the reference type '{self.type}'.")

    def generate_bibtex(self):
        bibtex = f"@{self.type}{{{self.id},\n"
        for field in self.required_fields.union(self.optional_fields):
            if hasattr(self, field):
                bibtex += f"  {field} = {{{getattr(self, field)}}},\n"
        bibtex += "}\n"
        return bibtex
