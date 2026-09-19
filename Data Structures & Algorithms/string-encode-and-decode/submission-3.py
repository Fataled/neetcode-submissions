class Solution:

    def encode(self, strs: List[str]) -> str:
        phrase = ""
        for word in strs:
            print(word)
            phrase += word
            phrase += "bkjre"
        
        return phrase
        
    def decode(self, s: str) -> List[str]:

        l = s.split("bkjre")[:-1]

        return l



