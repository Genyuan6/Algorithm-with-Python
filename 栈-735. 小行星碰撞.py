# 给定一个整数数组 asteroids，表示在同一行的小行星。
# 对于数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。
# 找出碰撞后剩下的所有小行星。碰撞规则：两个小行星相互碰撞，较小的小行星会爆炸。如果两颗小行星大小相同，则两颗小行星都会爆炸。两颗移动方向相同的小行星，永远不会发生碰撞。

# 示例 1：

# 输入：asteroids = [5,10,-5]
# 输出：[5,10]
# 解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
# 示例 2：

# 输入：asteroids = [8,-8]
# 输出：[]
# 解释：8 和 -8 碰撞后，两者都发生爆炸。
# 示例 3：

# 输入：asteroids = [10,2,-5]
# 输出：[10]
# 解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] #先弹出最后进入的元素，如[1,2,3] 则先弹出3
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast <0: #stack[-1]访问的是栈顶的元素，也就是列表的最后一个元素
                if abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(ast):
                    break
                else:
                    stack.pop()
            # else和循环结果一起使用的效果有些许不同，如果循环自然结束（即没有通过 break 语句中断），那么循环后的 else 块会被执行。如果循环是因为 break 语句而提前终止的，那么 else 块不会被执行。
            else:
                stack.append(ast)
        return stack
