class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        biggest =0
        for i in range(len(arr)):
            biggest = 0
            for j in range(i + 1, len(arr), 1):
                biggest = max(biggest, arr[j])
                arr[i] = biggest

        arr[-1] = -1

        return arr
                

        

            
