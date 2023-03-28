'''
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
'''

## Could be done in fewer lines..
def array_front9(nums):
    if len(nums) <= 4:
        if 9 in nums:
            return True
        else: 
            return False
    elif 9 in nums[0:4]:
        return True
    else:
        return False


#Simplified(?)
def array_front9_v2(nums):
    if len(nums) <= 4:
        nums = nums[len(nums)]
    else:
        nums = nums[0:4]
    
    return 9 in nums

