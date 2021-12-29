import re

class DisambiguatorSuffixRuleAn1(object):
    """
    afiks atau imbuhan yang terdapat pada akhir kata,
    contoh:
    tidak ada
    """

    def disambiguate(self, word):
        matches = re.match(r'^(.*)an$', word)
        if matches:
            return matches.group(1)

class DisambiguatorSuffixRuleNa1(object):
    """
    afiks atau imbuhan yang terdapat pada akhir kata,
    contoh:
    tidak ada
    """

    def disambiguate(self, word):
        matches = re.match(r'^(.*)na$', word)
        if matches:
            return matches.group(1)

class DisambiguatorSuffixRuleI1(object):
    """
    afiks atau imbuhan yang terdapat pada akhir kata,
    contoh:
    tidak ada
    """

    def disambiguate(self, word):
        matches = re.match(r'^(.*)i$', word)
        if matches:
            return matches.group(1)