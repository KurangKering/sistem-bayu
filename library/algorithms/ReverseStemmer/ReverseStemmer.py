import re

class ReverseStemmer(object):
    
    def __init__(self):
        pass
        self._init_transformation()
    
    def add_imbuhan(self, word):
        
        words = []
        for x in self.transformers:
            y = x.transform(word)
            if (y):
                words.append(y)
        
        return words
        
    def _init_transformation(self):
        self.transformers = []
        
        self.transformers.append(TransformInfixRuleEm1())
        self.transformers.append(TransformPrefixRuleNy1())
        self.transformers.append(TransformPrefixRuleNy2())
        self.transformers.append(TransformPrefixRuleN1())
        self.transformers.append(TransformPrefixRuleM1())
        self.transformers.append(TransformPrefixRuleNg1())
        self.transformers.append(TransformPrefixRuleKe1())
        self.transformers.append(TransformPrefixRuleDi1())
        self.transformers.append(TransformPrefixRuleMe1())
        self.transformers.append(TransformSuffixRuleAn1())
        self.transformers.append(TransformSuffixRuleNa1())
        self.transformers.append(TransformSuffixRuleI1())
        

class TransformInfixRuleEm1(object):
    """
    afiks atau imbuhan yang terdapat di dalam kata
    contoh :
    semaur  -> saur 
    gemuyu  -> guyu 
    """

    def transform(self, word):

        matches = re.match(r'^([^aiueo])([aiueo].*)$', word)
        if matches:
            return matches.group(1) + 'em' + matches.group(2)


class TransformPrefixRuleNy1(object):
    """
    Bentuk dasar diawali c
    contoh :
    nyuthat -> cuthat
    """
    def transform(self, word):

        matches = re.match(r'^c([aiueo].*)$', word)
        if matches:
            return 'ny' + matches.group(1)
        
class TransformPrefixRuleNy2(object):
    """
    Bentuk dasar diawali s
    contoh :
    nyilih -> silih
    """
    def transform(self, word):

        matches = re.match(r'^s([aiueo].*)$', word)
        if matches:
            return 'ny' + matches.group(1)
        
class TransformPrefixRuleN1(object):
    """
    Bentuk dasar diawali t
    contoh :
    negor -> tegor
    """
    def transform(self, word):

        matches = re.match(r'^t([aiueo].*)$', word)
        if matches:
            return 'n' + matches.group(1)
        
class TransformPrefixRuleM1(object):
    """
    Bentuk dasar diawali p
    contoh :
    mamah -> pamah
    """
    def transform(self, word):

        matches = re.match(r'^p([aiueo].*)$', word)
        if matches:
            return 'm' + matches.group(1)
        
class TransformPrefixRuleNg1(object):
    """
    Bentuk dasar diawali ng
    contoh :
    ngukur  -> kukur 
    """
    def transform(self, word):

        matches = re.match(r'^k([aiueo].*)$', word)
        if matches:
            return 'ng' + matches.group(1)
        
class TransformPrefixRuleKe1(object):
    """
    Bentuk dasar tidak tahu
    contoh :
    tidak ada
    """
    def transform(self, word):

        matches = re.match(r'^(.*)$', word)
        if matches:
            return 'ke' + matches.group(1)
        
class TransformPrefixRuleDi1(object):
    """
    Bentuk dasar tidak tahu
    contoh :
    tidak ada
    """
    def transform(self, word):

        matches = re.match(r'^(.*)$', word)
        if matches:
            return 'di' + matches.group(1)
        
class TransformPrefixRuleMe1(object):
    """
    Bentuk dasar tidak tahu
    contoh :
    tidak ada
    """
    def transform(self, word):

        matches = re.match(r'^(.*)$', word)
        if matches:
            return 'me' + matches.group(1)

import re

class TransformSuffixRuleAn1(object):
    """
    afiks atau imbuhan yang terdapat pada akhir kata,
    contoh:
    tidak ada
    """

    def transform(self, word):
        matches = re.match(r'^(.*)$', word)
        if matches:
            return matches.group(1) + 'an'

class TransformSuffixRuleNa1(object):
    """
    afiks atau imbuhan yang terdapat pada akhir kata,
    contoh:
    tidak ada
    """

    def transform(self, word):
        matches = re.match(r'^(.*)$', word)
        if matches:
            return matches.group(1) + 'na'

class TransformSuffixRuleI1(object):
    """
    afiks atau imbuhan yang terdapat pada akhir kata,
    contoh:
    tidak ada
    """

    def transform(self, word):
        matches = re.match(r'^(.*)$', word)
        if matches:
            return matches.group(1) + 'i'