# Write a Python program to find the nested lists elements, which are present in another list using lambda

def internested(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
print("\nIntersection of said nested lists:")
print(internested(nums1, nums2))