class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        right_product = []
        res = []
        for i,num in enumerate(nums):
            if i == 0:
                left_product.append(1)
            else:
                value = left_product[-1] * nums[i-1]
                left_product.append(value)
        print(left_product)
        
        size = len(nums)-1
        j = size
        while j >=0 :
            if j == size:
                right_product.append(1)
            else:
                value = right_product[-1] * nums[j+1]
                right_product.append(value)
            j -= 1
        # print(right_product)
        right_product.reverse()
        # print(right_product)
        for i in range(len(nums)):
            res.append(left_product[i] * right_product[i])
        
        return res
        

            
   
            