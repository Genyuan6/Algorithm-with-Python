# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
# 示例 1：
# 输入：arr = [1,2,2,1,1,3]
# 输出：true
# 解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
# 示例 2：
# 输入：arr = [1,2]
# 输出：false
# 示例 3：
# 输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
# 输出：true
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_table = {}
        for num in arr:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        # 比较出现次数是否是独一无二得
        occurances = list(hash_table.values())
        return len(occurances) == len(set(occurances))
            
