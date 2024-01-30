# 给你字符串 s 和整数 k 。
# 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
# 英文中的 元音字母 为（a, e, i, o, u）。
# 示例 1：
# 输入：s = "abciiidef", k = 3
# 输出：3
# 解释：子字符串 "iii" 包含 3 个元音字母。
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou") #排查元素是否在集合中，一般用set()
        max_count = count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1
            max_count = max(max_count, count) #要在for循环里面才行，才能实施更新最大的计数，不能放在for循坏外
        return max_count
