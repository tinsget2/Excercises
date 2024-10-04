import re


def regex_check_char(reg):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    bolReg = charRe.search(reg)
    return not bool(bolReg)


def a_followedby_0_orb(reg):
    pattern = '^a(b*)$'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def a_followedby_1_orb(reg):
    pattern = '^a(b+)$'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def a_followedby_0or1b(reg):
    pattern = '^a(b?)'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def a_followedby_2b(reg):
    pattern = 'ab{2}?'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def a_followedby_2or3b(reg):
    pattern = 'ab{2,3}?'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def lowercasefolowedby_(reg):
    pattern = '^[a-z]+_[a-z]+$'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def oneupperandlowwer(reg):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


def aendwithb(reg):
    pattern = 'a.*b$'
    if re.search(pattern, reg):
        return "Matched"
    else:
        return "Not matched"


results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12, 13, and 345 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

# print(aendwithb("aabbbbd"))
# print(aendwithb("aabAbbbc"))
# print(aendwithb("accddbbjjjb"))
# print(regex_check_char("ABCDEFabcdef123450"))
# print(regex_check_char("*&%@#!}{"))
# print(a_followedby_0_orb("ac"))
# print(a_followedby_0_orb("abc"))
# print(a_followedby_0_orb("a"))
# print(a_followedby_0_orb("ab"))
# print(a_followedby_0_orb("abb"))
# print(a_followedby_0or1b("a"))
# print(a_followedby_0or1b("abc"))
# print(a_followedby_0or1b("abbc"))
# print(a_followedby_0or1b("aabbc"))
# print(a_followedby_2b("abbb"))
# print(a_followedby_2b("aabbbbbc"))
# print(a_followedby_2or3b("ab"))
# print(a_followedby_2or3b("aabbbbbc"))
# print(lowercasefolowedby_("aab_cbbbc"))
# print(lowercasefolowedby_("aab_Abbbc"))
# print(lowercasefolowedby_("Aaab_abbbc"))
# print(oneupperandlowwer("AaBbGg"))
# print(oneupperandlowwer("Python"))
# print(oneupperandlowwer("python"))
# print(oneupperandlowwer("PYTHON"))
# print(oneupperandlowwer("aA"))
# print(oneupperandlowwer("Aa"))
