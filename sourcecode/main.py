import pandas as pd
import bibtexparser

bibtex_file_path = '../data/Projekt_BIB_original.txt'
excel_file_path = '../data/test.xlsx'

def bibtex_to_excel(bibtex_file_path, excel_file_path):
    # BIBTeX-Datei einlesen
    with open(bibtex_file_path, 'r', encoding='utf-8') as bibtex_file:
        bibtex_str = bibtex_file.read()

    # BIBTeX-Parser verwenden
    bib_database = bibtexparser.loads(bibtex_str)
    entries = bib_database.entries
    # print(entries, '\n\n')

    # DataFrame erstellen
    df = pd.DataFrame(entries)

    column_to_filter = 'year'
    df[column_to_filter] = df[column_to_filter].astype(str).str.replace('(\(|\))', '')

    # Daten in eine Excel-Datei schreiben und Formatierung steuern
    with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        worksheet = writer.sheets['Sheet1']
        # Setze die Zellenformatierung für die 'year'-Spalte auf Text
        worksheet.set_column('C:C', None, None, {'text_format': True})

# Beispielaufruf
bibtex_to_excel(bibtex_file_path, excel_file_path)
