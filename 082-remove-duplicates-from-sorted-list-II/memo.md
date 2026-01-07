## step1で考えたこと

前回の問題に重複しているNodeを削除する操作が追加

今回はprev, currが効果を発揮しそう

Psudo code

```py
while curr and curr.next:
    if curr.val == curr.next.val:
        curr = curr.next.next
        prev.next = curr
    else:
        prev = curr
        curr = curr.next
```

このままだと、三つ以上連続して重複がある時に壊れてしまう。

ここでどうするかで詰まった

## step1のコードを振り返って

3個以上だと

例：1 -> 2 -> 2 -> 2 -> 3

curr が最初の 2 を指す

curr.next.next は 3番目の 2

prev.next = curr すると、まだ 2 が残る

つまり「重複を全部消す」のに、重複が残ってしまう。

正解に辿り着くための考え方


1) 「重複の塊」を見つける

curr.val == curr.next.val を見つけた瞬間に、

curr が指している値 dup = curr.val が
連続している限り curr を進め続ける必要があった

2) head 自体が消えるケースがあるので dummy が必要

例：1 -> 1 -> 2 のとき、答えは 2。  
head が消える可能性があるので、prev=head だと破綻する。

### 削除が head にかかる可能性がある問題では prev は dummy からが鉄則