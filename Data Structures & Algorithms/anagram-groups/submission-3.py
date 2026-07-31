class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        result = {}
        for str in strs:
            counter = Counter(str)
            my_dict = tuple(sorted(counter.items()))
            print(f'counter is {my_dict}')
            if my_dict not in result:
                result[my_dict] = [str]
            else:
                result[my_dict].append(str)
        
        return list(result.values())