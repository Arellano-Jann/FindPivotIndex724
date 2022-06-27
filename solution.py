def pivotIndex1(nums): # 5%
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

def pivotIndex2(nums): # 12%
    final = [x for x in range(len(nums)) if sum(nums[:x]) == sum(nums[x+1:])]
    return -1 if len(final) == 0 else final[0]

def pivotIndex(nums): # 77%
    left, right = 0, sum(nums)
    for index, num in enumerate(nums):
        right -= num
        if left == right:
            return index
        left += num
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
print(pivotIndex([1, 2, 3]))
print(pivotIndex([-1, -1, -1, -1, -1, 0]))
print(pivotIndex([2,1,-1,-1,3]))
print(pivotIndex([-1,-1,-1,-1,-1]))
print(pivotIndex([-1,-1,-1,0,1,1]))