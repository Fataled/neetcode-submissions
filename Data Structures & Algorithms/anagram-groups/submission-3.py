class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = {}
        for words in strs:
            key = ''.join(sorted(words))
            if key in my_dict.keys():
                value = my_dict[key]
                value.append(words)
            else:
                my_dict[key] = [words]
            
        return list(my_dict.values())
    

                