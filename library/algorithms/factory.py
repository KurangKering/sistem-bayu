from .normalizer import BasicNormalizer, BayuNormalizer


class NormalisasiFactory:

    def create_bayu_normalizer(self, dictionary):

        basic =  BayuNormalizer(dictionary)
        return basic

    def create_basic_normalizer(self, dictionary):

        basic =  BasicNormalizer(dictionary)
        return basic
