"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = []
        first_index, second_index = 0, 0
        while first_index + second_index != len(nums1) + len(nums2):
            if first_index == len(nums1):
                merged_array.append(nums2[second_index])
                second_index += 1
                continue
            elif second_index == len(nums2):
                merged_array.append(nums1[first_index])
                first_index += 1
                continue
            elif nums1[first_index] <= nums2[second_index]:
                merged_array.append(nums1[first_index])
                first_index += 1
            else:
                merged_array.append(nums2[second_index])
                second_index += 1

        median_index = len(merged_array) // 2
        if len(merged_array) % 2 != 0:
            median = merged_array[median_index]
            print(merged_array)
            return median

        median = (merged_array[median_index] + merged_array[median_index - 1]) / 2
        print(merged_array)
        return median
