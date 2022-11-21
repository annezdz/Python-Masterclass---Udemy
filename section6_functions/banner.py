# USANDO DEFAULT PARAMETERS, podemos usar um valor diferente na chamada do método
def banner_text(text: str = '', width_size: int = 80) -> None:
    if len(text) > width_size - 4:
        print('EEK!!')
        print('THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH')

    if text == '*':
        print('*' * width_size)
    else:
        centred_text = text.center(width_size - 4)
        output_string = '**{0}**'.format(centred_text)
        print(output_string)


banner_text('*')
# podemos usar um valor diferente na chamada do método
banner_text('Always look on the bright side of life...')
# positional ou keywords
banner_text(width_size=100)
banner_text('The book is on the table...')

# banner_text('The book is on the table...', 100)

banner_text('*')

# result = banner_text('Nothin is returned')
# print(result)
