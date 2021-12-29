class ArrayDictionary(object):

    def __init__(self, words=None):
        self.words = {}
        if words:
            self.add_words(words)

    def contains(self, word):
        return word in self.words

    def count(self):
        return len(self.words)

    def add_words(self, words):
        self.words = dict(zip(words,words))

    def add(self, word):
        if not word or word.strip() == '':
            return
        self.words[word]=word





