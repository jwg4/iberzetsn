YIDDISH_LETTERS = [
    ("אֵ", "a"),
    ("אׇ", "o"),
    ("ב", "b"),
    ("ד", "d"),
    ("ה", "h"),
    ("ו", "u"),
    ("ט", "t"),
    ("י", "i"),
    ("כ", "kh"),
    ("ל", "l"),
    ("נ", "n"),
    ("ס", "s"),
    ("ע", "e"),
    ("ף", "f"),
    ("ר", "r"),
    ("ש", "sh"),
    ("ײ", "ey"),
]

YIDDISH_DOUBLE_LETTERS = [
    ("װ", "v"),
    ("ױ", "oy"),
]

YIDDISH_WORDS = [
    ("אויף", "af"),
]

YIDDISH_LETTER_LOOKUP = {
    x[0]: x[1] for x in YIDDISH_LETTERS + YIDDISH_DOUBLE_LETTERS
}

YIDDISH_WORD_LOOKUP = {
    x[0]: x[1] for x in YIDDISH_WORDS
}

ROMAN_LETTER_LOOKUP = {
    x[1]: x[0] for x in YIDDISH_LETTERS
}

ROMAN_DOUBLE_LETTER_LOOKUP = {
    x[1]: x[0] for x in YIDDISH_DOUBLE_LETTERS
}

ROMAN_ALIAS_LOOKUP = {
    "dd": "d"
}

ROMAN_COMPOSITE_LOOKUP = {
    "yi": "ייִ"
}

ROMAN_LOOKUP = ROMAN_LETTER_LOOKUP.copy()
ROMAN_LOOKUP.update(ROMAN_DOUBLE_LETTER_LOOKUP)
ROMAN_LOOKUP.update(ROMAN_COMPOSITE_LOOKUP)
ROMAN_LOOKUP.update({ x: ROMAN_LETTER_LOOKUP[ROMAN_ALIAS_LOOKUP[x]] for x in ROMAN_ALIAS_LOOKUP })
