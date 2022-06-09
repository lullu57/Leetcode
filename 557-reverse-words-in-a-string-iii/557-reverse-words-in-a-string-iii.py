class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()
        s = ""
        for i,word in enumerate(lst[::]):
            lst[i] = word[slice(None,None,-1)]
            s += lst[i] + " "
    
        return s[:-1:]