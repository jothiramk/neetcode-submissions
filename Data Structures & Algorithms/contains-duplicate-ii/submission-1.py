class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter_dict = {}
        for i,num in enumerate(nums):
            if num not in counter_dict:
                counter_dict[num] = i
            else:
                # if the element exists in the set already, find the index of that element
                index_one = counter_dict[num]
                if index_one != i and abs(index_one - i) <= k:
                    return True
                counter_dict[num] = i
            # print(counter_dict)
        return False
