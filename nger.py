
# next greater element to right


def nextGreaterElementToRight(nums1, nums2):
        res = []
        n = len(nums2)
        for i in nums1:
            temp = nums2.index(i)
            if temp == n-1:
                res.append(-1)
            elif (nums2[temp+1] > i):
                res.append(nums2[temp+1])
            else :
                flag = 0
                for j in range(temp+2 , n):
                    if (nums2[j] > i):
                        res.append(nums2[j])
                        flag = 1
                        break
                if flag == 0:
                    res.append(-1)
        return res


# next greater element to left


def nextGreaterElementToLeft(nums1, nums2):
        res = []
        n = len(nums2)
        for i in nums1:
            temp = nums2.index(i)
            if temp == n-1:
                res.append(-1)
            elif (nums2[temp+1] > i):
                res.append(nums2[temp+1])
            else :
                flag = 0
                for j in range(0,temp+2):
                    if (nums2[j] > i):
                        res.append(nums2[j])
                        flag = 1
                        break
                if flag == 0:
                    res.append(-1)
        return res
     

# next smaller element to left

def nextSmallerElementToLeft(nums1, nums2):
        res = []
        n = len(nums2)
        for i in nums1:
            temp = nums2.index(i)
            if temp == n-1:
                res.append(-1)
            elif (nums2[temp+1] > i):
                res.append(nums2[temp+1])
            else :
                flag = 0
                for j in range(0,temp+2):
                    if (nums2[j] < i):
                        res.append(nums2[j])
                        flag = 1
                        break
                if flag == 0:
                    res.append(-1)
        return res


# next smaller element to right
def nextSmallerElementToRight(nums1, nums2):
        res = []
        n = len(nums2)
        for i in nums1:
            temp = nums2.index(i)
            if temp == n-1:
                res.append(-1)
            elif (nums2[temp+1] > i):
                res.append(nums2[temp+1])
            else :
                flag = 0
                for j in range(temp+2 , n):
                    if (nums2[j] < i):
                        res.append(nums2[j])
                        flag = 1
                        break
                if flag == 0:
                    res.append(-1)
        return res


a = list(map(int, input("Enter array1").split()))
b = list(map(int, input("Enter array2").split()))
print("next greater element to right:  ",nextGreaterElementToRight(a,b))
print("next greater element to left:  ",nextGreaterElementToLeft(a,b))
print("next smaller element to right:  ",nextSmallerElementToRight(a,b))
print("next smaller element to left:  ",nextSmallerElementToLeft(a,b))

