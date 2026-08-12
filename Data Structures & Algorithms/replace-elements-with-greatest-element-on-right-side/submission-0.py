class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        size_arr = len(arr)
        for i  in range(len(arr)):
            if i == size_arr-1:
                arr[len(arr)-1]= -1
                break
            max_num = max(arr[i+1:])
            arr[i] = max_num
            
        return arr