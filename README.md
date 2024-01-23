## Projekt

### 1. Schritt
Analysieren Sie alle in BIBTeX vorkommenden Datenzusammenstellungen von Literaturquellen und
erstellen Sie ein allgemeingültiges Datenschema dafür. Das Schema sollte offen für Erweiterungen
und seine Darstellung für Nicht-XML-Kundige verständlich sein. (Mittel: Excel-Zellenstruktur /
Baumdiagramm / andere Visualisierungsform)

- [ ] Anschaulichen Excel
- - [ ] unnütze Klammern entfernen
- - [ ] andere unnötige Zeichen entfernen
- - [ ] Tabelle anschaulicher gestalten

### 2. Schritt
Entwurf einer XML-Struktur, die den Entwurf des gesamten Datenschemas von BIBTeX in XML
realisiert. (Ziel ist die Anzeige eines Literaturverzeichnisses im Stile einer mathematischen Zeitschrift,
entsprechend deren Gepflogenheiten und Stilvorgaben, siehe Beispiele.)

- [ ] XML

### 3. Schritt
Schreiben eines XSLT-Programmes, das den vorgegebenen Datenstrom (BiBTeX, XML_max) ausliest
und die Daten in Ihr XML-Schema überträgt. Alternativ können Sie auch Original-BiBTeXDateien
mit einer beliebigen Programmiersprache parsen und in Ihr XML-Schema übertragen. (Außerhalb
der Wertung.)
Validierung auf Vollständigkeit, Umgang mit Sonderzeichen und Umlauten, Umgang mit Zeilenumbrüchen
in BIBTeX-Daten, Umgang mit Fällen von Datenkapselung mit doppelten geschweiften
Klammern {{ oder }}, mit Sonderfällen der Datenstruktur. Ausschluss von komplizierten Sonderfällen
der gelieferten Beispielbibliothek, Begründung in Doku. Erstellung einer BIBTeX-Bibliothek/eines
XML-Dokuments ohne die Sonderfälle zur weiteren Bearbeitung des Projektes.
Erstellung von mehreren Testbibliotheken zur stufenweisen Implementierung von Features.

Alternative 1: Händische bzw. editor-teilautomatisierte Erzeugung einer datengefüllten XML-Datei
Ihres Types.
Alternative 2: Benutzung des BIBTeX-Parsers Ihrer Kommilitonen (ohne Gewähr) und anschließende
XSLT-Transformation des ausgegebenen XML-Stroms in die von Ihnen als sinnvoll erachtete XMLStruktur
(z.B. xsltproc benutzen).

- [ ] XSLT
- - [ ] unnütze Klammern entfernen
- - [ ] andere unnötige Zeichen entfernen

### 4. Schritt
Erstellung einer Document Type Definition (DTD) für Ihr XML-Schema. Test der DTD an immer
größeren Abschnitten der Beispielbibliothek.

- [ ] DTD

### 5. Schritt
Umsetzung der erarbeiteten DTD in eine XML-Schema-Definition (XSD) im Venetian Blind Design
unter Ausnutzung der sich ergebenden neuen Möglichkeiten. Test der XSD an immer größeren Abschnitten
der Beispielbibliothek. Verfeinerung der XSD je nach Notwendigkeit des angestrebten Projektziels.
Zeitaufwand:

- [ ] XSD

### 6. Schritt 
CSS-Datei/-Implementation oder XSL-Datei erarbeiten, um das Ergebnis Ihrer Arbeit in einem
Webbrowser darstellen zu können. Darstellung in zwei Webbrowsern, im Microsoft Edge oder im
Firefox oder in Google Chrome, erforderlich.
Als Darstellungsstil können Sie zwischen dem Stil der Zeitschrift für Analysis und ihre Anwendungen
(ZAA) und dem Stil der Mathematischen Nachrichten (MN) wählen, bei Dreiergruppen wählen Sie
sich ein weiteres mathematisches Journal mit unterschiedlichem Stil der Quellenangaben. Diese Stile
sind auf der Hausseite des Kurses DBS verlinkt. Der Stil der LNI ist nur zu Ihrer Information, wie
flexibel XSL-Dateien und XML-Dokumente (!) in der Realität gestaltet werden müssen.
- [ ] CSS
- [ ] zwei Webbrowser

### Abzugeben sind folgende Dateien: Mögliches Medium:

1.) Ihr Datenschema für BIBTeX-Bibliotheken allgemeiner Art, so dass XMLUnkundige den Aufbau der Daten verstehen.
Papier, PPT, Excel, Word
2.) Entwurf der XML-Struktur ohne Daten für BIBTeX-Bibliotheken allgemeiner Art
ASCII, Excel, Word, XML
3.) Ihr XML-Strom der konkreten BIBTEX-Bibliothek, die gegeben ist. Charakterisierung der von Ihnen ausgeschlossenen Datensätze mit Begründung.
(10% Maximum.)
XML-Datei, ASCII, Word, Excel
4.) DTD für die gegebene BIBTeX-Bibliothek, optional - für das gesamte XML-Schema
Die DTD ist validierbar mit einer Kopie des XML-Datenstroms zu verknüpfen.
XML-Datei, DTDDatei
5.) XSD für die gegebene BIBTeX-Bibliothek, optional - für das gesamte XML-Schema.
Die XSD ist im Design "Venetian Blind" zu schreiben und validierbar mit einer Kopie des XML-Datenstroms zu verknüpfen.
XML-Datei, XSDDatei
6.) CSS oder XSLT für die gegebene BIBTeX-Bibliothek, optional - für das gesamte XML-Schema.
XML-Datei, evtl. CSS-, XSL-Datei
7.) Dokumentation zu benötigten Veränderungen einer

## Fehlerbehebung

- pip install pandas
- pip install bibtexparser
- pip install openpyxl