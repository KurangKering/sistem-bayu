from library.algorithms.local_levenshtein import LocalLevenshtein
from library.algorithms import dictionary
from library.algorithms.ngram import BasicNGram
from library.algorithms.probability import BasicProbability
from library.algorithms.scoring import BasicScoring
from copy import deepcopy


class BayuNormalizer:

    def __init__(self, dictionary):

        levenshtein = LocalLevenshtein()

        self._normalizer = ImplementBayuNormalisasi(dictionary.as_list(), levenshtein)

    def normalisasi(self, words):
        output = self._normalizer.normalisasi(words)
        return output

class ImplementBayuNormalisasi:
    _sentence = ""
    _output = ""

    _dictionary_alg = None
    _levenshtein_alg = None

    def __init__(self, dictionary, levenshtein):
        self._dictionary_alg = dictionary
        self._levenshtein_alg = levenshtein

    def normalisasi(self, words):
        self._set_sentence(words)
        
        #1. lakukan stemming. jika ada, maka berhenti
        #2. jika tidak ada, maka stemming lagi, namun setiap perubahan kata dari hasil stemming
        # di simpan kemudian cek kata di kamus yang levenshtein setiap perubahan yang bernilai 1 terhadap hasil stemming tadi.
        #3. kata dasar yang punya levenshtein 1 tadi lalu diberi imbuhan lg.
        levenshtein = self._create_levenshtein(self._dictionary_alg, self._sentence)

        self._set_C_number(levenshtein)
        self._set_C(levenshtein)

        return self

    def _create_levenshtein(self, dictionary, sentence):
        levenshtein = self._levenshtein_alg.execute(dictionary, sentence)
        return levenshtein

    def _set_sentence(self, sentence):
        sentence = " ".join(sentence.split())
        self._sentence = sentence

    def _set_C(self, raw_C):
        self._C =  [list(x.keys()) for x in raw_C]

    def _set_C_number(self, raw_C):
        self._C_number = deepcopy(raw_C)

    def get_sentence(self):
        return self._sentence

    def get_C(self):
        return self._C

    def get_C_number(self):
        return self._C_number

    def get_output_str(self):
        return " ".join(self._output)


class BasicNormalizer:

    def __init__(self, dictionary):

        levenshtein = LocalLevenshtein()
        ngram = BasicNGram()
        prob = BasicProbability()
        scoring = BasicScoring()

        self._normalizer = ImplementBasicNormalisasi(dictionary.as_list(), levenshtein, ngram, prob, scoring)

    def normalisasi(self, words):
        output = self._normalizer.normalisasi(words)
        return output

class ImplementBasicNormalisasi:
    _C = []
    _C_number = []
    _W = []
    _sentence = ""
    _score = []
    _probability = []
    _grams = []
    _freqs = []
    _output = ""

    _dictionary_alg = None
    _ngram_alg = None
    _levenshtein_alg = None
    _probability_alg = None
    _scoring_alg = None

    def __init__(self, dictionary, levenshtein, ngram, prob, scoring):
        self._dictionary_alg = dictionary
        self._levenshtein_alg = levenshtein
        self._ngram_alg = ngram
        self._probability_alg = prob
        self._scoring_alg = scoring

    def normalisasi(self, words):
        self._set_sentence(words)
        self._set_W(self._sentence)

        levenshtein = self._create_levenshtein(self._dictionary_alg, self._sentence)
        self._set_C_number(levenshtein)
        self._set_C(levenshtein)

        self._grams, self._freqs = self._create_ngram(self._C, self._W)
        self._probability =  self._create_probability(self._C, (self._grams, self._freqs))
        self._score, self._output = self._create_scoring(self._C, self._probability)

        return self

    def _create_levenshtein(self, dictionary, sentence):
        levenshtein = self._levenshtein_alg.execute(dictionary, sentence)
        return levenshtein

    def _create_ngram(self, C, W):
        grams_freqs = self._ngram_alg.execute(C, W)
        return grams_freqs

    def _create_probability(self, C, grams_freqs):
        probability = self._probability_alg.execute(C, grams_freqs)
        return probability

    def _create_scoring(self, C, probability):
        scoring = self._scoring_alg.execute(C, probability)
        return scoring

    def _set_C(self, raw_C):
        self._C =  [list(x.keys()) for x in raw_C]

    def _set_C_number(self, raw_C):
        self._C_number = deepcopy(raw_C)

    def _set_W(self, sentence):
        token = sentence.split()
        self._W = deepcopy(token)
        self._W.insert(0,'_')
        self._W.insert(len(token)+1,'_')

    def _set_sentence(self, sentence):
        sentence = " ".join(sentence.split())
        self._sentence = sentence

    def get_C(self):
        return self._C

    def get_C_number(self):
        return self._C_number

    def get_W(self):
        return self._W

    def get_sentence(self):
        return self._sentence

    def get_grams(self):
        return self._grams

    def get_freqs(self):
        return self._freqs

    def get_score(self):
        return self._score

    def get_output(self):
        return self._output

    def get_output_str(self):
        return " ".join(self._output)

    def get_probability(self):
        return self._probability

