# This question is asked by Google. Given two integer arrays, return their intersection.
# Note: the intersection is the set of elements that are common to both arrays.

nums1 = input()
nums2 = input()

nums1 = nums1.split(' ')
nums1 = list(map(lambda x: int(x), nums1))
nums2 = nums2.split(' ')
nums2 = list(map(lambda x: int(x), nums2))

def intersection(nums1,nums2):
    hash={}
    result = []
    for num in nums1:
        if num not in hash:
            hash[num] = 1
    for num in nums2:
        if num in hash and hash[num]>0:
            hash[num] -= 1
            result.append(num)

    return result

print(intersection(nums1,nums2))
