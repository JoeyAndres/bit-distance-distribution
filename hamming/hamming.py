import itertools

from utility.dist import Dist


class Hamming(Dist):
    @staticmethod
    def dist(bits1, bits2):
        return sum(itertools.imap(lambda bit1, bit2: bit1 == bit2, bits1, bits2))
