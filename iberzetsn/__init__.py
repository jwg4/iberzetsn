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


def yiddish_to_roman(s):
    r = []
    for c in s:
        if c in YIDDISH_LETTER_LOOKUP:
            r.append(YIDDISH_LETTER_LOOKUP[c])
    return "".join(r)


def roman_to_yiddish(s):
    if not s:
        return ""
    prefixes = [ x for x in ROMAN_LOOKUP if s.startswith(x) ]
    if prefixes:
        prefixes.sort(key=len)
        x = prefixes[-1]
        return ROMAN_LOOKUP[x] + roman_to_yiddish(s[len(x):])
    raise ValueError("Couldn't find the first Yiddish character of %s" % (s, ))