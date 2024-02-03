import re
import latexcodec
import codecs
import latex2mathml.converter
import html


def clean_text(text):
    # If the text is not a string, return the text as is
    if not isinstance(text, str):
        return text

    # If the text is empty, return an empty string
    if text == '':
        return ''

    # Remove \bf LaTeX command
    text = re.sub(r'\\bf(?!\{)', '', text)

    # Remove \underline LaTeX command
    text = re.sub(r'\\underline(?!\{)', '', text)

    # Remove \it LaTeX command
    text = re.sub(r'\\it(?!\{)', '', text)

    # Decode LaTeX characters
    cleaned_text = text.encode('utf-8').decode('latex', 'ignore')

    # Remove characters like () and {}
    cleaned_text = re.sub(r'[()]', '', str(cleaned_text))
    cleaned_text = re.sub(r'[{}]', '', str(cleaned_text))
    cleaned_text = codecs.escape_decode(cleaned_text)[0].decode('utf-8')

    return cleaned_text


def latex_to_mathml(text):
    # Regular expression pattern for LaTeX formulas
    pattern = r'\$.*?\$'

    # Find all LaTeX formulas in the text
    formulas = re.findall(pattern, text)

    # If no formula is found, return the original text
    if not formulas:
        return text

    # Convert each formula to MathML and replace it in the text
    for formula in formulas:
        # Remove the $ signs from the formula
        formula_without_dollars = formula[1:-1]

        # Convert the formula to MathML
        mathml = latex2mathml.converter.convert(formula_without_dollars)

        # Replace the formula in the text with the MathML
        text = text.replace(formula, mathml)

    return text

