YIDDISH_LETTERS = {
    "ש": "sh",
    "ו": "u",
    "ל": "l",
}

def yiddish_to_roman(s):
    r = []
    for c in s:
        if c in YIDDISH_LETTERS:
            r.append(YIDDISH_LETTERS[c])
    return "".join(r)

def roman_to_yiddish(s):
    return ""