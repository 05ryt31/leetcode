## 問題文
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

## Step1で考えたこと
O(log n)という制約がある +　問題の特徴から -> Binary Search
Listを半分に分割し、右側の先頭の数字がTargetよりも大きければそのまま右側を走査、
小さければ左側を走査する
そのまま見つかればIndexをreturn

見つからない場合、

## Step2での気づき
解答解説を見た時、left, rightポインタを使えば良いのかと学んだ。

Let's look at the case where the target number is not present.

Input: nums = [1,3,5,6], target = 2
[1,3,5,6]
 L M   R
Now middle number is greater than the target, so move R to M - 1.

[1,3,5,6]
 L
 R
 M
Now middle number is less than the target, so move L to M + 1.

[1,3,5,6]
 R L
Now L is greater than R. We stop binary search. As a result, we don't find the target.

The description says "return the index where it would be if it were inserted in order."

In this case, we should insert the target into index 1. As you see, L is now at index 1, so

return 1 (= left index)

### Points
Return left index if you don't find the target.
見つからない場合のreturnするIndexの考え方も吸収できた。

### 間違えていたところとしては、
1. left <= rightとしていなかった。
2. right, leftの値更新の際の1ずらすところができていなかった。

right = mid - 1, left = mid + 1としないと、left < rightという制約を超えることがないため無限ループを引き起こしてしまう。

## GPTからもらった解答
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)  # 右端は“外”
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left  # 最初に target 以上が出る位置
```
target が配列内にあればその index、なければ挿入位置を返す  
target > 最後の要素 の場合でも left == len(nums) になって正しく 末尾 を返す.  
distinct でなくても“先頭の位置”が取れる（一般に強い）
