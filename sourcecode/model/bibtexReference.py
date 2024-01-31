from sourcecode.model.bibtexReferenceTypes import BibtexReferenceTypes as Reference


class BibtexReference:
    def __init__(self, citation_key, reference_type):
        self.citation_key = citation_key
        self.reference_type = reference_type.name  # Get the name of the Enum member as a string
        self.required_fields = set()
        self.optional_fields = set()

        # Assign required and optional fields based on the reference type
        if self.reference_type in Reference.__members__:  # Check if the name is a valid Enum member
            self.required_fields.update(Reference[self.reference_type].value["required_fields"])
            self.optional_fields.update(Reference[self.reference_type].value["optional_fields"])

    def add_field(self, field, value):
        # Check if the field is allowed for this reference type
        if field in self.required_fields or field in self.optional_fields:
            setattr(self, field, value)
        else:
            raise ValueError(f"Field '{field}' is not allowed for the reference type '{self.reference_type}'.")

    def generate_bibtex(self):
        bibtex = f"@{self.reference_type}{{{self.citation_key},\n"
        for field in self.required_fields.union(self.optional_fields):
            if hasattr(self, field):
                bibtex += f"  {field} = {{{getattr(self, field)}}},\n"
        bibtex += "}\n"
        return bibtex
