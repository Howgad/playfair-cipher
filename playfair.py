def prepare_text(text: str, filler='X') -> str:
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))
    prepared = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else filler
        if a == b:
            prepared += a + filler
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += filler
    return prepared

def generate_matrix(key: str) -> list[list[str]]:
    key = key.upper().replace('J', 'I')
    key = ''.join(dict.fromkeys(filter(str.isalpha, key)))
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = list(dict.fromkeys(key + alphabet))
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return -1, -1

def playfair_cipher(text: str, key: str, mode='encrypt') -> str:
    matrix = generate_matrix(key)
    text = prepare_text(text)
    result = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            if mode == 'encrypt':
                result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            else:
                result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            if mode == 'encrypt':
                result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result