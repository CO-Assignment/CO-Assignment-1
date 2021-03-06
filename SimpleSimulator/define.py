pc = 0
memory = []

# Dictionary storing opcodes with their corresponding operator
opcodes = {
    "00000": "add",
    "00001": "sub",
    "00010": "movI",
    "00011": "movR",
    "00100": "ld",
    "00101": "st",
    "00110": "mul",
    "00111": "div",
    "01000": "rs",
    "01001": "ls",
    "01010": "xor",
    "01011": "or",
    "01100": "and",
    "01101": "not",
    "01110": "cmp",
    "01111": "jmp",
    "10000": "jlt",
    "10001": "jgt",
    "10010": "je",
    "10011": "hlt",
}


# Dictionary that stores register values.
registerStored = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0,
}
