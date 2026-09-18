class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_dict = {}
        
        
        for i,n in enumerate(strs):
            my_list = []
            for l in n:
                my_list.append(l)
            my_list = sorted(my_list)
            key = ''.join(my_list)
            if key in my_dict.keys():
                value = my_dict[key]
                value.append(strs[i])
            else:
                my_dict[key] = [strs[i]]
            
        return list(my_dict.values())

                