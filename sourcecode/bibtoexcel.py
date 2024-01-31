import pandas as pd
import bibtexparser
import re
import latexcodec

bibtex_file_path = 'data/Projekt_BIB_original.txt'
excel_file_path = 'data/test.xlsx'


def clean_text(text):
    # Remove characters like () and {}
    cleaned_text = re.sub(r'[(){}]', '', str(text))
    # cleaned_text = cleaned_text.replace(r'\bf', '')
    cleaned_text = cleaned_text.encode('latin-1').decode('latex', 'ignore')
    return cleaned_text


def bibtex_to_excel(bibtex_file_path, excel_file_path):
    # BIBTeX-Datei einlesen
    with open(bibtex_file_path, 'r', encoding='utf-8') as bibtex_file:
        bibtex_str = bibtex_file.read()

    # BIBTeX-Parser verwenden
    bib_database = bibtexparser.loads(bibtex_str)
    entries = bib_database.entries

    # DataFrame erstellen
    df = pd.DataFrame(entries)

    # Apply clean_text function to all columns
    df = df.apply(lambda col: col.map(clean_text) if col.dtype == 'O' else col)

    # Daten in eine Excel-Datei schreiben und Formatierung steuern
    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        worksheet = writer.sheets['Sheet1']
        # Setze die Zellenformatierung für die 'year'-Spalte auf Text
        worksheet.set_column('C:C', None, None, {'text_format': True})

        # Create format objects for bold, underline, and italic text
        bold_format = writer.book.add_format({'bold': True})
        underline_format = writer.book.add_format({'underline': True})
        italic_format = writer.book.add_format({'italic': True})

        # Iterate over the DataFrame and check each cell for the presence of LaTeX commands
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                cell_value = df.iat[row, col]
                if isinstance(cell_value, str):
                    format = None
                    if '\\bf' in cell_value:
                        cell_value = cell_value.replace('\\bf', '')
                        format = bold_format
                    if '\\underline' in cell_value:
                        cell_value = cell_value.replace('\\underline', '')
                        format = underline_format
                    if '\\it' in cell_value:
                        cell_value = cell_value.replace('\\it', '')
                        format = italic_format
                    if format:
                        # If a command is found, apply the corresponding format to the cell in Excel
                        worksheet.write(row + 1, col, cell_value, format)
                    else:
                        worksheet.write(row + 1, col, cell_value)


# Beispielaufruf
bibtex_to_excel(bibtex_file_path, excel_file_path)
