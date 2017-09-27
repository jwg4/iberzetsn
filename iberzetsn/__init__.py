from .letters import YIDDISH_LETTER_LOOKUP, ROMAN_LOOKUP


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