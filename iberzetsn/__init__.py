from .letters import YIDDISH_LETTER_LOOKUP, YIDDISH_WORD_LOOKUP, ROMAN_LOOKUP


def yiddish_to_roman(s):
    if not s:
        return ""
    if " " in s:
        words = s.split(" ")
        return " ".join(yiddish_to_roman(w) for w in words)
    if s in YIDDISH_WORD_LOOKUP:
        return YIDDISH_WORD_LOOKUP[s]
    r = []
    b = ""
    for c in s:
        if c in YIDDISH_LETTER_LOOKUP:
            r.append(YIDDISH_LETTER_LOOKUP[c])
        elif b + c in YIDDISH_LETTER_LOOKUP:
            r.append(YIDDISH_LETTER_LOOKUP[b + c])
        else:
            b = c
    return "".join(r)


def roman_to_yiddish(s):
    if not s:
        return ""
    if " " in s:
        words = s.split(" ")
        return " ".join(roman_to_yiddish(w) for w in words)
    prefixes = [ x for x in ROMAN_LOOKUP if s.startswith(x) ]
    if prefixes:
        prefixes.sort(key=len)
        x = prefixes[-1]
        return ROMAN_LOOKUP[x] + roman_to_yiddish(s[len(x):])
    raise ValueError("Couldn't find the first Yiddish character of %s" % (s, ))
