## step1で考えたこと

それぞれの括弧に対応するものを取り除いていき、最後に残っていればFalse, そうでないならTrue

=> whileの終了条件をどうするか？
無限ループになってしまう
さらにStep1のコードだと本来FalseであるべきものもTrueになってしまう

カッコを分けて取り除くのではなく、セットで取り除けば良いのでは？？

## step2
コードは適切に求められたことを処理できているがRuntimeが若干遅いのが気になる
Time Complexity: O(n^2). 
Space Complexity: O(n). 
=> Brute Force


もっと早くするにはどうすべきか
- whileを使わないで書く
=> Using stack

## step3
