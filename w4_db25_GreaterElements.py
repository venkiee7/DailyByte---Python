# This question is asked by Amazon. Given two arrays of numbers, where the first array is a subset of the second array, return an array containing all the next greater elements for each element in the first array, in the second array. If there is no greater element for any element, output -1 for that number.

nums1 = input()
nums2 = input()

nums1 = nums1.split(' ')
nums1 = list(map(lambda x: int(x), nums1))
nums2 = nums2.split(' ')
nums2 = list(map(lambda x: int(x), nums2))

def nextGreaterElement(nums1, nums2):
  map = {}
  stack = []
  for i in range(len(nums1)):
    map[nums1[i]] = i
    
  for i in range(len(nums2) - 1, -1, -1):
    if nums2[i] in map:
      while len(stack) > 0 and stack[-1] <= nums2[i]:
        stack.pop()
      if len(stack) == 0:
        map[nums2[i]] = -1
      else:
        map[nums2[i]] = stack[-1]
    stack.append(nums2[i])

  results = []
  for num in nums1:
    results.append(map[num])
  return results

print(nextGreaterElement(nums1, nums2))