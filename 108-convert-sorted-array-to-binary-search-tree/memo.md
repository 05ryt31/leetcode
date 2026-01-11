## step1で考えたこと
root nodeをどう決めるか？ => numsの中央値を取る？

Binary Searchが使えるわけではなさそう？

middleが中心のIndexとなるからそれの一個ずらした左右のIndexをleft, rightとして、端に寄せていくイメージ

## step1に対するフィードバック
- bst.left = nums[left] / bst.right = nums[right] って int を入れてしまっていて、TreeNode をつないでない（木になってない）
- そもそもどんどん左に、右にnodeを増やしていったらそれはHeight-Balancedではないのでは？
