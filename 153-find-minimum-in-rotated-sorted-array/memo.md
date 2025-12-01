## 問題文
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

## step1で考えたこと
1回rotateすると、一番後ろのnumberが先頭に来て、それ以降が一つずれる
1ずつIndexをずらすには？
Binary Searchを使った解法が思いつかない

return the minimum element of this array.
-> この部分に関してはsortしたListの先頭をただreturnすれば良いのでは？

## step1でのコード
```py
class Solution:
    def findMin(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        min = sorted_nums[0]
        rotate_time = 0

        while nums != sorted_nums:
            sorted_nums = 
            rotate_time += 1
        
        return min

```

## step2での気づき
やはり、大小を比較するときに、=を含めるか否かが判断できていない。
returnの位置を間違えていた。