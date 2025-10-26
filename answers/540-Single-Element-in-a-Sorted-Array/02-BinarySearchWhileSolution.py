class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        while (left < right):
            mid = int(left + (right - left) / 2) #compensating for overflow
            isEven = (right - mid) % 2 == 0

            if(nums[mid] == nums[mid - 1]): #verifying if the number is equal to the previous 
                if isEven:
                    right = mid - 2 #trying to ignore the duplicate element
                else:
                    left = mid + 1
            
            elif(nums[mid] == nums[mid + 1]): #verifying if the number is equal to the foward position 
                if isEven:
                    left = mid + 2 #trying to ignore the duplicate element
                else:
                    right = mid - 1
            
            else:
                return nums[mid]
        return nums[left]