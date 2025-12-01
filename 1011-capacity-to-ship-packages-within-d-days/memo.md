## Time Complexity O(Nlog(Sum))

## step1で考えたこと
daysと同じ数のパーテーションに分ける.  
totalを使ってDaysで割った値は意味がなさそう.  
どうやって機械にパーテーションを分けさせるか  

### Hint1を見た
-> Binary search on the answer. We need a function possible(capacity) which returns true if and only if we can do the task in D days.

10分考えたものの、手付かずで解答を見た。

## step2で書いたコードの問題点
### ミス1：積み方の条件が完全に間違っている
```py
if current_weight < cap:
    current_weight += w
else:
    needed_day += 1
```
正しくは：
今積んでいる重さ + 次の荷物 <= cap なら積める

つまり：
```py
if current_weight + w <= cap:
    current_weight += w
else:
    needed_day += 1
    current_weight = w
```
とすべき。

### ミス2：二分探索の範囲更新が逆
```py
if is_shipable(mid):
    min_cap = mid + 1
else:
    max_cap = mid - 1
```
これは 「条件を満たす中で“最大の値”」を探す形。
実際にやりたいのは：

is_shipable(mid) で条件を満たしたらもっと小さい容量でも実現できるか試す.  
→ right を mid へ寄せるべき

正しくはこう：
```py
if is_shipable(mid):
    max_cap = mid
else:
    min_cap = mid + 1
```

なぜ、max_capをmid - 1ではなくmidで止めるのか？  
is_shipable(mid) が True のとき、mid 自体が答えの可能性があるから。  
だから mid を捨てず、探索区間に残す必要がある。

## 関数を定義せずに書くとこうなる（参考）
-> 見た目は綺麗だが、個人的には読みにくく直感的ではないと思った。
```py
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left
```