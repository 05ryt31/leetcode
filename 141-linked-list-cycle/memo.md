## step1で考えたこと
前にやったことがある気がする
l, rポインタを使い、l = rとなれば has cycle(True).  
ならずに終わればFalse

## step2
二つのポインタを使う方針はあっていたが、left, rightではなく、slow, fastを使う問題だった。
- head[-1]は存在しない。ListNodeだから
cycle判定では両方ともheadからスタートする。

step2では動いて、正解ではあるが、若干Runtimeが遅い => これはただ言語の問題か？

Time Complexity: O(n)

Space Complexity: O(1)