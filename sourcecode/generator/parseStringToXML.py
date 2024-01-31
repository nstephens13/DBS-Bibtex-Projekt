import html
import unicodedata
import re
import latexcodec


def convert_latex_to_string(input_string):
    # Normalize the input string, replacing LaTeX symbols with their corresponding characters
    normalized_string = unicodedata.normalize('NFKD', input_string)

    # Remove any remaining LaTeX commands
    output_string = ''
    skip_next = False
    for char in normalized_string:
        if skip_next:
            skip_next = False
            continue
        if char == '\\':
            skip_next = True
            continue
        output_string += char

    return output_string


def convert_to_xml_readable(input_string):
    # Convert LaTeX to a string and replace special characters with their XML character references
    input_string = html.escape(convert_latex_to_string(input_string))

    # Replace non-ASCII characters
    output_string = ''
    for char in input_string:
        if ord(char) > 127:  # Non-ASCII character
            try:
                # Get the Unicode name of the character
                unicode_name = unicodedata.name(char)

                # Create a numeric character reference for the character
                char = '&#{};'.format(ord(char))
            except ValueError:
                pass  # No Unicode name, use the original character
        output_string += char

    return output_string


def clean_text(text):
    # Remove characters like () and {}
    cleaned_text = re.sub(r'[(){}]', '', str(text))
    # cleaned_text = cleaned_text.replace(r'\bf', '')
    cleaned_text = cleaned_text.encode('latin-1').decode('latex', 'ignore')
    return cleaned_text

# Example usage
input_string = '{Birkh\"auser, Boston - Basel - Berlin}'
print(convert_latex_to_string(input_string))
print(convert_to_xml_readable(input_string))
print(clean_text(input_string))
