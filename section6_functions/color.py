BLACK = '\u001b[30m '
RED = '\u001b[31m '
GREEN = '\u001b[32m '
YELLOW = '\u001b[33m '

RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    Print text using the ANSI sequences to change colour.
    :param text: The text to print.
    :param effects: The effect we want
    """
    effect_strings = "".join(effects) #faz o join de efeitos
    output_string = '{0}{1}{2}'.format(effect_strings, text, RESET)
    print(output_string)


colour_print('Hello', RED)
colour_print('Hello', RED, REVERSE)
colour_print('Hello', RED, REVERSE, UNDERLINE)

colour_print('Hello', GREEN)
colour_print('Hello', YELLOW)
colour_print('Hello', YELLOW, BOLD)

