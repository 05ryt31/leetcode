## step1で考えたこと
所要時間；13分

Binary Searchが使えそう

最初にRoot Node二つを与えて、関数を使い回す

新しいTreeを作るのに変数が必要？ => Tree1のvalを上書きしていけばいいのでは？

## step1へのフィードバック
- 「Binary Searchが使えそう」→ ここでは使わない。
これは木の値の大小を使って探す問題じゃなくて、構造を同時にたどる DFS（再帰）が本筋。

- 「Tree1を上書きしていけばいいのでは？」→ その方針はOK

### 書いたコードの問題点
1) while node1 is not None or node2 is not None: がダメ

この while の中で node1 / node2 を進めてないので、条件が変わらず 無限ループになる。
この問題は「ループで横に走査」ではなく「左右の子へ降りる」なので、while は不要

2) if node1 is None: node1.val = node2.val が不可能

node1 is None なのに node1.val にアクセスしている。確実に落ちる。

node1 が None のときは、

その位置は node2 をそのまま返すが正しい処理

3) node2 が None の可能性を無視

node1.val += node2.val は node2 が None なら落ちます。
なのでベースケースは

node1 が None → node2 を返す

node2 が None → node1 を返す

が必須。

## step2で間違えていたこと
再帰の結果を子のNodeに代入していなかった