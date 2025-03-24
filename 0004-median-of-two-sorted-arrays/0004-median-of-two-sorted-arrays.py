class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1.extend(nums2)
        # nums1.sort()
        # n = len(nums1)
        # if n%2==1:
        #     return float(nums1[n//2])
        # else:
        #     return float(nums1[n//2] + nums1[n//2-1])/2 
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1+n2
        new_arr = [0 for _ in range(n)]
        i = 0
        j = 0
        k = 0
        while i < n1 and j < n2 and k < n:
            if nums1[i] < nums2[j]:
                new_arr[k] = nums1[i]
                i += 1
            else:
                new_arr[k] = nums2[j]
                j += 1
            k += 1
        # print(i, j, k, new_arr)
        while i < n1 and k < n:
            new_arr[k] = nums1[i]
            i += 1
            k += 1
        # print(i, j, k, new_arr)
        while j < n2 and k < n:
            new_arr[k] = nums2[j]
            j += 1
            k += 1
        # print(new_arr)
        if n%2==1:
            return float(new_arr[n//2])
        else:
            return float(new_arr[n//2] + new_arr[n//2-1])/2 
