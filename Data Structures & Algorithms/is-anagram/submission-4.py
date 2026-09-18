class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list()
        s2 = list()

        for letters in s:
            s1.append(letters)
        
        for l in t:
            s2.append(l)

        s1 = sorted(s1)
        s2 = sorted(s2)
        
        return (s1 == s2)

        