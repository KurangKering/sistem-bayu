import re

class DisambiguatorInfixRuleEm1(object):
    """
    afiks atau imbuhan yang terdapat di dalam kata
    contoh :
    semaur  -> saur 
    gemuyu  -> guyu 
    """

    def disambiguate(self, word):

        matches = re.match(r'^([^aiueo])em([aiueo].*)$', word)
        if matches:
            return matches.group(1) + matches.group(2)