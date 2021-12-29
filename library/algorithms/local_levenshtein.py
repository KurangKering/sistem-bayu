from library.algorithms.Levenshtein import distance

class LocalLevenshtein:

    _dict = None
    _max_op = 5

    def execute(self, dictionary, sentence):
        self._dict = dictionary
        result = self.process(sentence)
        return result

    def process(self, text):

        words = text.split(' ')
        result = []

        for word in words:
            result.append(self.process_word(word))

        return result

    def process_word(self, word):
        result = {}
        proceed = self.real_process(word)
        if proceed == []:
            return result

        condition = True
        count = 0
        while (condition):
            result = {k: v for k, v in proceed if v == count}

            condition = (result == {}) and (count < self._max_op)
            count = count + 1

        return result

    def real_process(self, word):

        output = []
        # checked_word = [x for x in self._dict.as_list() if x.startswith(word[0])]
        checked_word = [x for x in self._dict]
        for dict_word in checked_word:
            num_of_process = self.singular_levenshtein(word, dict_word)
            if num_of_process is None:
                continue
            temp = (dict_word, num_of_process)
            output.append(temp)

        output = sorted(output, key=lambda tup: tup[1])

        return output

    def singular_levenshtein(self, word1, word2):
        num = distance(word1, word2)
        return num

