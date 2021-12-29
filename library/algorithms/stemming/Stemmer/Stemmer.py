import re
from library.algorithms.stemming.Stemmer.Context.Visitor.VisitorProvider import VisitorProvider
from library.algorithms.stemming.Stemmer.Filter import TextNormalizer
from library.algorithms.stemming.Stemmer.Context.Context import Context

class Stemmer(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.visitor_provider = VisitorProvider()

    def get_dictionary(self):
        return self.dictionary

    def stem(self, text):
        normalizedText = TextNormalizer.normalize_text(text)

        words = normalizedText.split(' ')
        stems = []

        for word in words:
            stems.append(self.stem_word(word))

        return ' '.join(stems)

    def stem_word(self, word):
        return self.stem_singular_word(word)

    def stem_singular_word(self, word):
        context = Context(word, self.dictionary, self.visitor_provider)
        context.execute()

        return context.result

