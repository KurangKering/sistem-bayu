class DontStemShortWord(object):

    def visit(self, context):
        if self.is_whort_word(context.current_word):
            context.stopProcess()

    def is_whort_word(self, word):
        return len(word) <= 3




