import random

standard_qwerty = [
    {
        "lower": ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', None, None],
        "upper": ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', None, None]
    },
    {
        "lower": [None, None, 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
        "upper": [None, None, 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|']
    },
    {
        "lower": [None, None, None,'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', None],
        "upper": [None, None, None,'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"', None]
    },
    {
        "lower": [None, None, None, None,'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', None],
        "upper": [None, None, None, None, 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', None]
    },
]

l33t = {
    'a' : ['a', 'A', '@', '4'],
    'b' : ['b', 'B', '8'],
    'c' : ['c', 'C'],
    'd' : ['d', 'D'],
    'e' : ['e', 'E', '3'],
    'f' : ['f', 'F'],
    'g' : ['g', 'G', '&', '6', '9'],
    'h' : ['h', 'H'],
    'i' : ['i', 'I', '!', '1'],
    'j' : ['j', 'J'],
    'k' : ['k', 'K'],
    'l' : ['l', 'L', '1'],
    'm' : ['m', 'M'],
    'n' : ['n', 'N'],
    'o' : ['o', 'O', '0'],
    'p' : ['p', 'P'],
    'q' : ['q', 'Q'],
    'r' : ['r', 'R'],
    's' : ['s', 'S', '5'],
    't' : ['t', 'T', '7'],
    'u' : ['u', 'U'],
    'v' : ['v', 'V'],
    'w' : ['w', 'W'],
    'x' : ['x', 'X'],
    'y' : ['y', 'Y'],
    'z' : ['z', 'Z']
}

def get_key_index(key, keyboard):
    for row_index, row in enumerate(keyboard):
        for case in ['lower', 'upper']:
            if key in row[case]:
                col_index = row[case].index(key)
                return {
                    "row": row_index,
                    "case": case,
                    "column": col_index
                }
    return None
   
def standard_deviation(word, keyboard):
    cipher = []

    for key in word:
        key_info = get_key_index(key, keyboard)
        if not key_info:
            continue

        row = key_info['row']
        col = key_info['column']

        for i in range(row, -1, -1):
            try:
                temp = keyboard[i]['lower'][col]
                if temp is not None:
                    cipher.append(temp)
            except IndexError:
                continue

        for i in range(0, row + 1):
            try:
                temp = keyboard[i]['upper'][col]
                if temp is not None:
                    cipher.append(temp)
            except IndexError:
                continue

    return ''.join(cipher)

def hackerman(leet, subs):
    cipher = []
    for key in leet:
        try:
            cipher.append(subs[key][random.randint(0, len(subs[key]) - 1)])
        except KeyError:
            continue

    return ''.join(cipher)

while True:
    user_input = input("Input: ").lower()
    if user_input == 'exit':
        break
    print(f"Walk: {standard_deviation(user_input, standard_qwerty)}\nHackerman: {hackerman(user_input, l33t)}\n")
    
