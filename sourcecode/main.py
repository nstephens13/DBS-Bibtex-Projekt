import pandas as pd
import bibtexparser
import re

bibtex_file_path = '../data/Projekt_BIB_original.txt'
excel_file_path = '../data/test.xlsx'

def clean_text(text):
    # Remove characters like () and {}
    cleaned_text = re.sub(r'[(){}]', '', str(text))
    cleaned_text = cleaned_text.replace(r'\bf', '')
    #cleaned_text = cleaned_text.replace(r'h\"a', 'ä')
    cleaned_text = cleaned_text.encode('latin-1').decode('latex')
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

# Beispielaufruf
bibtex_to_excel(bibtex_file_path, excel_file_path)
