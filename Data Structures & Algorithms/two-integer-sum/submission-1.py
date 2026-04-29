class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        return_val = [0, 0]
        # what should keys and values be? 
        # key should be index, value should be value 
        for i in range (len(nums)):
            difference = target - nums[i]

            if difference in hashmap:
                return_val[0] = hashmap[difference]
                return_val[1] = i
                return return_val
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            
                    

