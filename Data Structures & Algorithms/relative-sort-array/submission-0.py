class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)


        result = []
        for num in arr2:
            if num in freq:
                result.extend([num]*freq[num])
                del freq[num]
        temp_result = []
        for key,value in freq.items():
            temp_result.extend([key]*value)
        return result + sorted(temp_result)