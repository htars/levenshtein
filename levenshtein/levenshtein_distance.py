from functools import lru_cache


class Levenshtein:

    @classmethod
    @lru_cache(maxsize=4096)
    def calc_distance(cls, s, t):
        '''calculate levenshtein distance between two strings.'''

        # if one of the characters is empty, the length of the other is the
        # distance you want.
        if not s: return len(t)
        if not t: return len(s)

        # if the first letter is a match, the distance after the second letter
        # is the distance you want.
        if s[0] == t[0]: return cls.calc_distance(s[1:], t[1:])

        # calulate the cost for the rest of the string.
        
        # add to top of s
        l1 = cls.calc_distance(s, t[1:])

        # delete to top of s
        l2 = cls.calc_distance(s[1:], t)

        # replace the beginning of the s
        l3 = cls.calc_distance(s[1:], t[1:])

        # consumption of cost 1 with add/delete/replace implemented is fixed.
        # add the minimum cost for the rest of the strings to get the distance.
        return 1 + min(l1, l2, l3)

    @classmethod
    def calc_standardization(cls, s, t):
        return cls.calc_distance(s, t) / max(len(s), len(t))

    @classmethod
    def calc_similarity(cls, s, t):
        return - cls.calc_standardization(s, t) + 1
