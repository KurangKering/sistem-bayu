from library.algorithms.stemming.Stemmer.Context.Visitor.AbstractDisambiguatePrefixRule import AbstractDisambiguatePrefixRule

class PrefixDisambiguator(AbstractDisambiguatePrefixRule):

    def __init__(self, disambiguators):
        super(PrefixDisambiguator, self).__init__()

        self.add_disambiguators(disambiguators)



