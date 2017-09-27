YIDDISH_LETTERS = [
    ("ש", "sh"),
    ("ו", "u"),
    ("ל", "l"),
    ("ד", "d"),
    ("י", "i"),
]

YIDDISH_LETTER_LOOKUP = {
    x[0]: x[1] for x in YIDDISH_LETTERS
}

ROMAN_LETTER_LOOKUP = {
    x[1]: x[0] for x in YIDDISH_LETTERS
}

ROMAN_ALIAS_LOOKUP = {
    "dd": "d"
}

ROMAN_COMPOSITE_LOOKUP = {
    "yi": "ייִ"
}

ROMAN_LOOKUP = ROMAN_LETTER_LOOKUP.copy()
ROMAN_LOOKUP.update(ROMAN_COMPOSITE_LOOKUP)
ROMAN_LOOKUP.update({ x: ROMAN_LETTER_LOOKUP[ROMAN_ALIAS_LOOKUP[x]] for x in ROMAN_ALIAS_LOOKUP })
