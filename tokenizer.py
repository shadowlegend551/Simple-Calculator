def tokenize(args):
    operators = ['+', '-', '(', ')', '*', '/', '^']
    output = []
    currenttoken = ''

    for char in args:
        if char not in operators:
            currenttoken += char
        elif char in operators:
            if currenttoken != '':
                output.append(int(currenttoken))
                currenttoken = ''
            output.append(char)

    if currenttoken != '':
        try:
            output.append(int(currenttoken))
        except TypeError:
            output.append(currenttoken)
    return output