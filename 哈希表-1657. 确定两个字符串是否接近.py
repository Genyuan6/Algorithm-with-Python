# 如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：
# 操作 1：交换任意两个 现有 字符。
# 例如，abcde -> aecdb
# 操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
# 例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
# 你可以根据需要对任意一个字符串多次使用这两种操作。
# 给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
# 示例 1：
# 输入：word1 = "abc", word2 = "bca"
# 输出：true
# 解释：2 次操作从 word1 获得 word2 。
# 执行操作 1："abc" -> "acb"
# 执行操作 1："acb" -> "bca"
# 示例 2：
# 输入：word1 = "a", word2 = "aa"
# 输出：false
# 解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
# 示例 3：
# 输入：word1 = "cabbba", word2 = "abbccc"
# 输出：true
# 解释：3 次操作从 word1 获得 word2 。
# 执行操作 1："cabbba" -> "caabbb"
# 执行操作 2："caabbb" -> "baaccc"
# 执行操作 2："baaccc" -> "abbccc"
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        # 统计每个字符串中字符的出现次数
        def count_chars(word):
            char_count = {}
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            return char_count

        count1 = count_chars(word1)
        count2 = count_chars(word2)

        # 检查字符集是否相同
        if set(count1.keys()) != set(count2.keys()):
            return False
        # 统计每个字符串中出现次数的频率
        #例如 word1=“aaabbbbccddeeeeefffff”, word2 = "aaaaabbcccdddeeeeffff",如果都用set(count1.values())和set(count2.values())来分析的话两者出现次数的集合都是{2，3，4，5},会被误判为True,但具有相同出现次数的字符数量却不相同，如word1中出现2次的字符有两个，而word2中只有一个，这样并不能够实现操作2的要求
        def count_freq(count_dict):
            freq_count = {}
            for count in count_dict.values():
                if count in freq_count:
                    freq_count[count] += 1
                else:
                    freq_count[count] = 1
            return freq_count

        freq1 = count_freq(count1)
        freq2 = count_freq(count2)

        # 检查出现次数的频率是否相同
        return freq1 == freq2 #并不用考虑键的顺序
