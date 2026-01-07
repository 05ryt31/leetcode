## step1で考えたこと

prev, currを使って、比較する

prev == currであれば、prevのnextをNoneとし、currを使っていく

これを最後まで続ける

## step2
### step1で書いたコードを振り返って

prev と curr は ノード（オブジェクト） なので、prev == curr は「同じノードか」になりがちです。

重複判定は 値でやるので

```py
prev.val == curr.val
```

```py
prev.next = None
prev = curr
```
としていて、リストを途中で切断してしまった.  
やりたいのは「重複ノードを飛ばす」ことだから

```py
prev.next = curr.next
curr = curr.next
```

みたいに curr を削除して prev を残すのが基本

Time Comp: O(n)
Space Comp: O(1)