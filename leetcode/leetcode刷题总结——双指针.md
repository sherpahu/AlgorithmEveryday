# leetcode刷题总结——双指针

双指针是用两个指针去遍历数组或链表。

分为对撞指针（首尾双指针）、快慢指针（同向双指针）、反向双指针、分离双指针这几种

## 1. 对撞指针：

- 定义：又称为首尾双指针，有两个指针front,tail分别指向开始和结尾，front增加，tail减少，向中间“对撞”，在此过程中判断是否出现满足条件的和。

- 用途：用于求解数组中满足条件的两个节点，若求多个数则先固定n-2个位置。

  例如在[三数之和](<https://leetcode-cn.com/problems/3sum/>)中将顺序遍历三个数中最小的索引，固定最小索引时将中间的索引和最后的索引作为双指针。

- 使用注意事项：为保证不漏，需要对数组进行排序。为保证没有重复，需要将指针移动到不相邻的元素上。

两个指针分别称为front,tail

#### [三数之和](https://leetcode-cn.com/problems/3sum/)

<https://leetcode-cn.com/problems/3sum/>

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rst=[]
        #双指针，k<i<j
        nums.sort()
        for k in range(len(nums)-3+1):
            if nums[k]>0:
                break
                #k最小，nums[k]>0则不可能得到和为0，提前剪枝
            if k>0 and nums[k]==nums[k-1]:
                continue
                #避免重复
            i,j=k+1,len(nums)-1#对撞指针
            while i<j:
                s=nums[k]+nums[i]+nums[j]
                #print(s)
                if s>0:
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif s<0:
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                else:
                    rst.append([nums[k],nums[i],nums[j]])
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
        return rst
```

### [最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)

<https://leetcode-cn.com/problems/3sum-closest/>

```python
import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_sum=sys.maxsize
        nums.sort()
        for left in range(len(nums)-2):
            mid=left+1
            right=len(nums)-1
            delta=target-nums[left]
            while mid<right:
                delta_all=target-nums[left]-nums[mid]-nums[right]
                if abs(delta_all)<abs(target-min_sum):
                    min_sum=nums[left]+nums[mid]+nums[right]
                    
                if delta_all==0:
                    return nums[left]+nums[mid]+nums[right]
                elif delta_all>0:
                    mid+=1
                    while mid<right and nums[mid]==nums[mid-1]:mid+=1
                else:
                    right-=1
                    while mid<right and nums[right]==nums[right+1]:right-=1
        return min_sum
```



## 2. 快慢指针

- 定义：又称为同向双指针，都从开始

#### [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

<https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/submissions/>

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while fast<len(nums):
            nums[slow]=nums[fast]
            while fast<len(nums) and nums[fast]==nums[slow]:
                fast+=1
            slow+=1
        return slow
```









## 5. 分离双指针

- 定义：输入两个数组或链表，求其交集或者合并两个容器时，在两个容器中分别设立两个指针独立移动。

### [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

<https://leetcode-cn.com/problems/merge-two-sorted-lists/submissions/>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=head=ListNode(-1)
        while l1 and l2:
            if l1.val<l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
        rest=l1 or l2
        while rest:
            head.next=rest
            head=head.next
            rest=rest.next
        return dummy.next
```

