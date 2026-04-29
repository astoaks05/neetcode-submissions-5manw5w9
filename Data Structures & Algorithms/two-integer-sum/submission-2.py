class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        # what should keys and values be? 
        # key should be index, value should be value 
        for i, num in enumerate(nums):
            dif = target - num
            if dif in hashmap:
                return([hashmap[dif], i])
            hashmap[num] = i
            
                    

