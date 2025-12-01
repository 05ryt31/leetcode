## 問題文
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## step1で考えたこと
以前NeetCodeで似たような問題を解いていたのと、Treeに関する問題の解き方がある程度わかっていたため、  
解答の方針は立てれた。  
Pythonを久しぶりに書いているため文法が怪しい。

## step2での気づき

### 誤解1：Python では null ではなく Noneを使う。
問題文のArrayにnullが入っていたためそこに引っ張られていた。

### 誤解2：dfs(node.left) and dfs(node.right) は間違い

and で二つの再帰結果を返そうとしているが  
→ Python の and は真偽値演算子であり、最大深度を返さない  
→ 深さ比較が行われていない  
→ 再帰が破壊される 

最大深度は 左右の深さの max を返す：

return 1 + max(dfs(node.left), dfs(node.right))

dfsの関数を定義する必要性がそもそもなかった。maxDepth自身を使えば良い。

### BFSを使った実装
```py
from collections import deque

def maxDepth(root):
    if root is None:
        return 0
    
    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):   # 今のレベルのノード数だけ回す
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth

```

#### なぜ、Dequeを使うのか？
-> 高速で安全にキューが作れるから

Tree の BFS（幅優先探索）はキュー構造が必要。

キューの操作はたった2つ：
1. enqueue（末尾に追加）
2. dequeue（先頭から取り出す）

もし list をキューとして使うと...  
list の先頭から pop(0) すると O(n) かかる
```py
queue = [1,2,3,4]
queue.pop(0)
```

pop(0) をすると：

[2, 3, 4]   
↑ 全部1つ左にずらす必要がある

つまり、リストの先頭を pop するたびに全要素がシフトしてしまう。

BFS ではノード数ぶん pop するので、大きな木だと性能がどんどん悪くなる。

---

deque なら先頭の pop が O(1)
dequeは 両端から高速に追加・削除できるデータ構造。
```py
from collections import deque

queue = deque([1,2,3,4])
queue.popleft()    # O(1)
```

内部で「両端アクセスに特化した双方向連結リスト」を使っているため、
pop(0) に相当する操作も O(1) で超高速。