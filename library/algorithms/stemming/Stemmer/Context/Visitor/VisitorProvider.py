from library.algorithms.stemming.Stemmer.Context.Visitor.DontStemShortWord import DontStemShortWord
from library.algorithms.stemming.Stemmer.Context.Visitor.PrefixDisambiguator import PrefixDisambiguator

from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorPrefix import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorInfix import *
from library.algorithms.stemming.Morphology.Disambiguator.DisambiguatorSuffix import *

class VisitorProvider(object):

    def __init__(self):
        self.visitors = []
        self.suffix_visitors = []
        self.infix_visitors = []
        self.prefix_visitors = []
        self.prefix_pemanis_visitors = []
        self.prefix_penanda_visitors = []
        self.prefix_persona_visitors = []

        self.init_visitors()

    def init_visitors(self):
        # self.visitors.append(DontStemShortWord())
        
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleAn1()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleNa1()]))
        self.suffix_visitors.append(PrefixDisambiguator([DisambiguatorSuffixRuleI1()]))


        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleNy1()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleNy2()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleN1()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleM1()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleNg1()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleKe1()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleDi1()]))
        self.prefix_visitors.append(PrefixDisambiguator([DisambiguatorPrefixRuleMe1()]))


        self.infix_visitors.append(PrefixDisambiguator([DisambiguatorInfixRuleEm1()]))


    def get_visitors(self):
        return self.visitors

    def get_suffix_visitors(self):
        return self.suffix_visitors

    def get_prefix_visitors(self):
        return self.prefix_visitors

    def get_infix_visitors(self):
        return self.infix_visitors

