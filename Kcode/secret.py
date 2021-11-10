__info__ = """
kcode = encode message using keybord indexing 

<< encode process:

msg -->
    kcode -->
        utf-8 encode --> *** hex ***

>> decode process:

encoded_msg -->
    hex-->
        utf-8 decode -->
            kcode --> *** msg ***
"""


_encode_dict = {
    'a': 'Q',
    'b': 'W',
    'c': 'E',
    'd': 'R',
    'e': 'T',
    'f': 'Y',
    'g': 'U',
    'h': 'I',
    'i': 'O',
    'j': 'P',
    'k': 'A',
    'l': 'S',
    'm': 'D',
    'n': 'F',
    'o': 'G',
    'p': 'H',
    'q': 'J',
    'r': 'K',
    's': 'L',
    't': 'Z',
    'u': 'X',
    'v': 'C',
    'w': 'V',
    'x': 'B',
    'y': 'N',
    'z': 'M',
    ' ': '~',
    '1': '0',
    '2': '1',
    '3': '2',
    '4': '3',
    '5': '4',
    '6': '5',
    '7': '6',
    '8': '7',
    '9': '8',
    '0': '9',
    'A': 'q',
    'B': 'w',
    'C': 'e',
    'D': 'r',
    'E': 't',
    'F': 'y',
    'G': 'u',
    'H': 'i',
    'I': 'o',
    'J': 'p',
    'K': 'a',
    'L': 's',
    'M': 'd',
    'N': 'f',
    'O': 'g',
    'P': 'h',
    'Q': 'j',
    'R': 'k',
    'S': 'l',
    'T': 'z',
    'U': 'x',
    'V': 'c',
    'W': 'v',
    'X': 'b',
    'Y': 'n',
    'Z': 'm',
}
_decode_dict = {str(_encode_dict[k]):k for k in _encode_dict.keys()}