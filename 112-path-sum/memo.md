## step1で考えたこと

Sumをどうやって渡していくか？関数呼び出しの時に渡すのが良さそう。となるとHelper関数が必要か

self.checkPathSum(root, current_sum)を呼ぶタイミングがどこが適切かがわからない。今の場合だとまだ定義されていないから呼べないよと怒られる。

hasTarget = (current_sum == turgetSum)

この部分で、三項演算子的なものを使って書きたかったがわからなかった。文法的にあっているかもわからない。

## step1へのフィードバック
内側関数はself不要

leafで判定するとより良い￥

合計を渡す代わりに残りのtargetを減らすやり方の方が賢かった

### 参考にした他の人のコード

#### https://github.com/mamo3gr/arai60/pull/24/
再帰の考え方は同じだったが、Queueを使って書くという新しい発想が得られた。
is_leafの議論も面白い。自分も欲しい派

Queueを使ったコードも読みやすい印象を持った。

#### https://github.com/plushn/SWE-Arai60/pull/25/

減法を使って書いていたコード、ほとんど同じ