class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(filter(str.isalnum, s)).lower()
        n= ""

        for l in range(len(s) -1, -1, -1):
            n += s[l]
    


        return s == n