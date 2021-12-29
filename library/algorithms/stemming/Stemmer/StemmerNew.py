import re
from library.algorithms.stemming.Stemmer.Context.Visitor.VisitorProvider import VisitorProvider
from library.algorithms.stemming.Stemmer.Filter import TextNormalizer
# from library.algorithms.stemming.Stemmer.Context.Context import Context
from library.algorithms.stemming.Stemmer.Context.ContextNew import ContextNew as Context

class Stemmer(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.visitor_provider = VisitorProvider()
        self.guess_words = []
        self.found = []

    def get_dictionary(self):
        return self.dictionary

    def stem(self, text):
        normalizedText = TextNormalizer.normalize_text(text)
        self.guess_words = []
        self.found = []
        
        words = normalizedText.split(' ')
        stems = []

        for word in words:
            temp = self.stem_word(word)
            
            self.guess_words.append(temp['guess_words'])
            stems.append(temp['result'])
        return ' '.join(stems)

    def get_guess_words(self):
        return self.guess_words
    
    def stem_word(self, word):
        return self.stem_singular_word(word)

    def stem_singular_word(self, word):
        context = Context(word, self.dictionary, self.visitor_provider)
        context.execute()
        guess_words = [x for x in list(set(context.get_guess_words())) if x is not None]
        result = context.result
        if (context.result == context.current_word):
            self.found.append(True)
        else:
            self.found.append(False)

        return {'result':result, 'guess_words':guess_words}

