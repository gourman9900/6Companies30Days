from collections import defaultdict
class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        index = defaultdict(list)
        for word in words:
            index["".join(sorted(word))].append(word)
        return index.values()
        #code here
