import os
from library.algorithms.stemming.Dictionary.ArrayDictionary import ArrayDictionary
# from library.algorithms.stemming.Stemmer.Stemmer import Stemmer
from library.algorithms.stemming.Stemmer.StemmerNew import Stemmer
from library.algorithms.stemming.Stemmer.CachedStemmer import CachedStemmer
from library.algorithms.stemming.Stemmer.Cache.ArrayCache import ArrayCache

class StemmerFactory(object):
    APC_KEY = 'cache_dictionary'

    def create_stemmer(self, isDev=False, kamusClass=None):
        """ Returns Stemmer instance """

        words = kamusClass.get_kamus()
        dictionary = ArrayDictionary(words)
        stemmer = Stemmer(dictionary)

        resultCache = ArrayCache()
        cachedStemmer = CachedStemmer(resultCache, stemmer)

        return stemmer

    def get_words(self, isDev=False):
        #if isDev or callable(getattr(self, 'apc_fetch')):
        #    words = self.getWordsFromFile()
        #else:
        #    words = apc_fetch(self.APC_KEY)
        #    if not words:
        #        words = self.getWordsFromFile()
        #        apc_store(self.APC_KEY, words)
        return self.get_words_from_file()

    def get_words_from_file(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dictionaryFile = current_dir + '/data/kata-dasar.txt'
        if not os.path.isfile(dictionaryFile):
            raise RuntimeError('Dictionary file is missing. It seems that your installation is corrupted.')

        dictionaryContent = ''
        with open(dictionaryFile, 'r') as f:
            dictionaryContent = f.read()

        return dictionaryContent.split('\n')