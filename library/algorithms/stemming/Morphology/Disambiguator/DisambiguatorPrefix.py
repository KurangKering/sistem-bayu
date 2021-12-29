import re



class DisambiguatorPrefixRuleNy1(object):
    """
    Bentuk dasar diawali c
    contoh :
    nyuthat -> cuthat
    """
    def disambiguate(self, word):

        matches = re.match(r'^ny([aiueo].*)$', word)
        if matches:
            return 'c' + matches.group(1)
        
class DisambiguatorPrefixRuleNy2(object):
    """
    Bentuk dasar diawali s
    contoh :
    nyilih -> silih
    """
    def disambiguate(self, word):

        matches = re.match(r'^ny([aiueo].*)$', word)
        if matches:
            return 's' + matches.group(1)
        
class DisambiguatorPrefixRuleN1(object):
    """
    Bentuk dasar diawali t
    contoh :
    negor -> tegor
    """
    def disambiguate(self, word):

        matches = re.match(r'^n([aiueo].*)$', word)
        if matches:
            return 't' + matches.group(1)
        
class DisambiguatorPrefixRuleM1(object):
    """
    Bentuk dasar diawali p
    contoh :
    mamah -> pamah
    """
    def disambiguate(self, word):

        matches = re.match(r'^m([aiueo].*)$', word)
        if matches:
            return 'p' + matches.group(1)
        
class DisambiguatorPrefixRuleNg1(object):
    """
    Bentuk dasar diawali ng
    contoh :
    ngukur  -> kukur 
    """
    def disambiguate(self, word):

        matches = re.match(r'^ng([aiueo].*)$', word)
        if matches:
            return 'k' + matches.group(1)
        
class DisambiguatorPrefixRuleKe1(object):
    """
    Bentuk dasar tidak tahu
    contoh :
    tidak ada
    """
    def disambiguate(self, word):

        matches = re.match(r'^ke(.*)$', word)
        if matches:
            return matches.group(1)
        
class DisambiguatorPrefixRuleDi1(object):
    """
    Bentuk dasar tidak tahu
    contoh :
    tidak ada
    """
    def disambiguate(self, word):

        matches = re.match(r'^di(.*)$', word)
        if matches:
            return matches.group(1)
        
class DisambiguatorPrefixRuleMe1(object):
    """
    Bentuk dasar tidak tahu
    contoh :
    tidak ada
    """
    def disambiguate(self, word):

        matches = re.match(r'^me(.*)$', word)
        if matches:
            return matches.group(1)
