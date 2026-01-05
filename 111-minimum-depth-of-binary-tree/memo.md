## step1で考えたこと
前回の問題104と同様にしたら解けるのではないかと思い、testしてみるとこのtestケースでFailしてしまうことに気づいた。  

Input: root = [2,null,3,null,4,null,5,null,6]  
Output: 1  
Expected: 5  　　

この結果を受け、最初のroot.left or root.rightがNoneの場合どう扱うかが鍵ということに気づいた。

Validationをどう行うか？
```py
if root.left is None or root.right is None:
    return
```
この場合のreturn値をどうするか？

## step2
通るコードにはなったがまだ無駄が多い、もっとシンプルに、早くできそう

## step3
LeetcodeのSolutionで他の言語で実装されていたのを見つけたのでPythonで実装してみたが、見た目はシンプルで分かりやすいがパフォーマンスは2と比べ、悪化した。

どうやら最も良いパフォーマンスを実現するにはBFSを採用した方が良いみたい。
```py
class Solution:
    def minDepth(self, root):
        '''
        For any binary tree, not just BST
        number of nodes >= 0
        '''

        if not root:
            return 0

        q = deque()
        q.append((root, 1))

        res = float("inf")

        while q:
            x,y = q.popleft()

            if x.left or x.right:
                if x.left:
                    q.append((x.left, y+1))
                if x.right:
                    q.append((x.right, y+1))

            else:
                res = y
                break

        return res
```